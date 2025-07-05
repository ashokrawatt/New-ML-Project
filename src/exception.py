import sys 
import logging


def error_massege_detail(error, error_detail:sys):
    _,_,exe_tb = error_detail.exe_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_massege = "error occured in python script name [{0}] line number [{1}] error massege [{2}]" .format(
     file_name,exe_tb.tb_lineno,str(error)
    
    )
    
    return error_massege
    
    
class CustomException(Exception):
    def __init__(self,error_massege, error_detail:sys):
        super().__init__(error_massege)
        self.error_massege=error_massege_detail(error_massege,error_detail=error_detail)
        
        
    def __str__(self):
        return self.error_massege
    
    
if __name__=="__main__":
        
    try:
        a= 1/0
    except Exception as e:
        logging.info("devide by zero")
        raise CustomException(e,sys)
     
     
     