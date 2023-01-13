from azure.common.credentials import ServicePrincipalCredentials
from azure.graphrbac import GraphRbacManagementClient

from loguru import logger

import traceback


try:

    credentials = ServicePrincipalCredentials(
        client_id="28d4f4eb-5c8b-4655-8465-e233e71ac3c8",
        secret="pvB8Q~yNQX0~VxnUmnGqHnd.CkEW0f.mtEJUIa7G",
        resource="https://graph.windows.net",
        tenant='pravalikareddy6yahoo.onmicrosoft.com'
    )

    data = {
        'grant_type': 'client_credentials',
        'client_id': "your_client_id",
        'scope': 'https://graph.microsoft.com/.default',
        'client_secret': "your_client_secret"
    }

    tenant_id = '809e51ec-39d6-419c-90b7-377fb590142f'

    graphrbac_client = GraphRbacManagementClient(
        credentials,
        tenant_id
    )

    # users = graphrbac_client.users.list()
    # for user in users:
    #     print(user.user_principal_name)

    groups = graphrbac_client.groups.list()
    for g in groups:
        print(g.display_name)


except Exception as e:
    logger.error(traceback.print_exc())
