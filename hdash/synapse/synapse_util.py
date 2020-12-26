import synapseclient
from hdash.synapse.credentials import SynapseCredentials


class SynapseUtil:
    MASTER_HTAN_TABLE = "cache/master_htan.csv"
    MASTER_HTAN_ID = "syn20446927"

    def __init__(self):
        self.syn = synapseclient.Synapse()
        self.cred = SynapseCredentials()
        self.syn.login(self.cred.user, self.cred.password, silent=True)

    def retrieve_master_htan_table(self):
        master_htan_table = self.syn.tableQuery(
            "SELECT * FROM %s" % SynapseUtil.MASTER_HTAN_ID
        )
        df = master_htan_table.asDataFrame()
        df.to_csv(SynapseUtil.MASTER_HTAN_TABLE)

    def retrieve_file(self, synapse_id):
        syn_link = self.syn.get(entity=synapse_id)
        return syn_link.path