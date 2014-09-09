from utils import *
from testcases.rhsmgui.rhsmguibase import RHSMGuiBase
from testcases.rhsmgui.rhsmguilocator import RHSMGuiLocator
from testcases.rhsmgui.rhsmconstants import RHSMConstants
from utils.exception.failexception import FailException

class tc_ID178118_GUI_display_orgname_and_identity(RHSMGuiBase):

    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % self.__class__.__name__)
        try:
            try:
                username = RHSMConstants().get_constant("username")
                password = RHSMConstants().get_constant("password")
                self.open_subscription_manager()
                self.register_and_autosubscribe_in_gui(username, password)
                self.click_view_system_facts_menu()
                self.click_facts_view_tree("system")
                if self.check_org_displayed_in_facts(username, password):
                    logger.info("It's successful to check orgs displayed in system facts in GUI ")
                else:
                    raise FailException("Test Faild - Failed to check orgs displayed in system facts in GUI")
                if self.check_system_uuid_displayed_in_facts():
                    logger.info("It's successful to check system_uuid displayed in system facts in GUI ")
                else:
                    raise FailException("Test Faild - Failed to check system_uuid displayed in system facts in GUI")
                return 0
            except Exception, e:
                logger.error("Test Failed - ERROR Message:" + str(e))
                return -1
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    tc_ID178118_GUI_display_orgname_and_identity().test_run()
