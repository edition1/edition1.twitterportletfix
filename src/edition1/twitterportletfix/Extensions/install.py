import logging

logger = logging.getLogger('edition1.twitterportletfix')


def uninstall(portal, reinstall=False):
    if not reinstall:
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile(
            'profile-edition1.twitterportletfix:uninstall')
        logger.info("Uninstall done")
