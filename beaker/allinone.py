from beaker.bkrhsm import BKRHSMLEVEL1, BKRHSMLEVEL2
from beaker.bkrhsmstage import BKRHSMSTAGELEVEL1, BKRHSMSTAGELEVEL2
from beaker.bkrhsmgui import BKRHSMGUI
from beaker.bksaminstall import BKSAMInstall
from utils.installation.vwkscreate import VWKSCreate
from beaker.bkvirtwhokvm import BKvirtwhoKVM
from beaker.bkvirtwhoesx import BKvirtwhoESX
from beaker.bkvirtwhoxenfv import BKvirtwhoXENFV
from beaker.bkvirtwhoxenpv import BKvirtwhoXENPV

class AllInOne():

    def start(self):
        new_rhel, build = VWKSCreate().start()
        new_sam, sam_build, sam_server = BKSAMInstall().start()
        if new_rhel == 0 or new_sam == 0:
            # run stage testing only new rhel comes
            if new_rhel == 0:
                BKRHSMSTAGELEVEL1().start(build)
            # if no sam new build, install the latest one
            if new_sam == -1:
                new_sam, sam_build, sam_server = BKSAMInstall().start(sam_build)
            BKRHSMLEVEL1().start(build, sam_build, sam_server)
            BKRHSMLEVEL2().start(build, sam_build, sam_server)
            BKRHSMGUI().start(build, sam_build, sam_server)
            BKvirtwhoKVM().start(build, sam_build, sam_server)
            BKvirtwhoESX().start(build, sam_build, sam_server)
            BKvirtwhoXENFV().start(build, sam_build, sam_server)
            BKvirtwhoXENPV().start(build, sam_build, sam_server)

if __name__ == "__main__":
    AllInOne().start()
