#BEGIN_HEADER
import logging
import os
from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER

class kb_diamond:
    '''
    Module Name:
    kb_diamond
    Module Description:
    A KBase module: kb_diamond
    '''

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    #END_CLASS_HEADER

    def __init__(self, config):
        #BEGIN_CONSTRUCTOR

        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        
        #END_CONSTRUCTOR
        pass

    def run_kb_diamond(self, params):
        #BEGIN run_kb_diamond
        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': params['parameter_1']},
                                                'workspace_name': params['workspace_name']})
        output = {
                'report_name': report_info['name'],
                'report_ref': report_info['ref'],
        }
        #END run_kb_diamond

    def status(self):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                        'message': "",
                        'version': self.VERSION,
                        'git_url': self.GIT_URL,
                        'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS