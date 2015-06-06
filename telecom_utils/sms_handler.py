__author__ = 'RAJAT'

#This module handles the SMS PDU generation ( Encoding ) and field
#information generation from a SMS PDU ( Decoding)


from messaging.sms import SmsSubmit
from messaging.sms import SmsDeliver

class SmsEncoder():
    """
    This class generates the PDU from the given SMS fields
    """
    def __init__(self, encodingType, smscAddress, pduType, smsText, address ):
        self._smsPdu = ""
        self._encodingType = encodingType
        self._smscAddress = smscAddress
        self._pduType = pduType
        self._smsText = smsText
        self._address = address

    def generateSmsDeliverPdu(self):
        pass

    def generateSmsSubmitPdu(self):
        smsPdus = []
        smsDelvObj = SmsSubmit(self._address, self._smsText)
        smsDelvObj._set_csca(self._smscAddress)
        print("Encoding Type:", self._encodingType)
        if ( self._encodingType == 0):
            smsDelvObj.dcs = 0x00
        if ( self._encodingType == 8):
            smsDelvObj.dcs = 0x08

        for i in smsDelvObj.to_pdu():
            smsPdus.append(i.pdu)
        return smsPdus

    def generateSmsPdu(self):
        #this method generates the  SMS PDU
        #1 stand for SMS_SUBMIT
        if ( self._pduType == 1):
            #generate PDU of SMS_SUBMIT
            smsPdus = self.generateSmsSubmitPdu()
            return smsPdus

        if (self._pduType == 2):
            #generate PDU of type SMS_DELIVER
            self.generateSmsDeliverPdu()
        else:
            return "Invlaid PDU type"


    def verifySmscAddress(self,smsc):
        pass

    def verifyEncodingType(self,encodingType):
        pass

    def verifyPduType(self,pduType):
        pass

    def verifyAddress(self, address):
        pass


