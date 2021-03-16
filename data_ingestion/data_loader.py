import pandas as pd
from AzureBlobStorage.azureBlobStorage import AzureBlobStorage
from MongoDB.mongoDbDatabase import mongoDBOperation


class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training.
    """
    def __init__(self, file_object, logger_object):
        self.training_file = 'InputFile.csv'
        self.file_object = file_object
        self.logger_object = logger_object
        self.dbObj = mongoDBOperation()
        self.azureObj = AzureBlobStorage()

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception
        """

        self.logger_object.log(self.file_object,'Entered the get_data method of the Data_Getter class')
        try:
            self.data = self.azureObj.csvToDataframe('Training_FileFromDB', self.training_file)
            print('Dataframe Loaded')
            self.logger_object.log(self.file_object,'Data Load Successful.Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_data method of the Data_Getter class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            raise Exception()