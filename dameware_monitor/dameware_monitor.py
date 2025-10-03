import sys, datetime, psutil
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import QTimer

DAMEWARE_PORT = 6129
PROCESS_NAME = "DWRCS.exe"
LOOPBACKS = {"127.0.0.1", "::1"}

def dameware_pids():
    pids = []
    for p in psutil.process_iter(["name", "pid"]):
        if (p.info["name"] or "").lower() == PROCESS_NAME.lower():
            pids.append(p.info["pid"])
    return set(pids)

def remote_peers_owned_by_dameware():
    """回傳由 DWRCS.exe 擁有、且不是本機位址的 ESTABLISHED 連線清單"""
    peers = []
    pids = dameware_pids()
    if not pids:
        return peers

    for c in psutil.net_connections(kind="tcp"):
        if (
            c.laddr and c.laddr.port == DAMEWARE_PORT and
            c.status == psutil.CONN_ESTABLISHED and
            c.pid in pids and
            c.raddr and c.raddr.ip not in LOOPBACKS
        ):
            peers.append(f"{c.raddr.ip}:{c.raddr.port}")
    return peers

class Watcher:
    def __init__(self):
        self.prev = 0
        self.t = QTimer()
        self.t.setInterval(2000)
        self.t.timeout.connect(self.poll)
        self.t.start()

    def poll(self):
        peers = remote_peers_owned_by_dameware()
        if self.prev == 0 and len(peers) > 0:
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            QMessageBox.warning(None, "DameWare 警告",
                                f"偵測到 DameWare 連線！\n時間：{ts}\n遠端：{', '.join(peers)}")
        self.prev = len(peers)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Watcher()
    sys.exit(app.exec())
