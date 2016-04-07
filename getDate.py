#--------------------------------------------------------------------------
# Drew Wilson
# 2016/04/07
# Code that gives an example of how to call upon an MXServer class
# and then inside a definition, grab the getDate function.
#--------------------------------------------------------------------------

from psdi.mbo import MboConstants
from psdi.server import MXServer

def changeStatus(mbo, newStatus):
    #--------------------------------------------------------------------------
    # Initialize variables
    #--------------------------------------------------------------------------
    
    # use the mboLogger so our log messages are captured with Maximo's messages
    # for the MBO passed in by the Launch Point
    mboLogger = mbo.getMboLogger()
    
    # Capture the current date and time when the status changed.
    newStatusDate = MXServer.getMXServer().getDate()
    
    #alternative method, does the same thing
    server = MXServer.getMXServer()
    newModifiedDate = server.getDate()
    
    
    #------------------------------------------------------------------------------
    # Update the status attributes on this Mbo.
    #------------------------------------------------------------------------------
    
    mbo.setValue("STATUSDATE", newStatusDate, MboConstants.NOACCESSCHECK)
    mbo.setValue("STATUS", newStatus, MboConstants.NOACCESSCHECK)
    mbo.setValue("SQLSCRIPT", "/*%s\n*/\n\n%s" % (getVarsInScope(), mbo.getString("SQLSCRIPT")))
    
    #------------------------------------------------------------------------------
    # Logs our SQL's change in status. You are calling a different mbo with the
    # relationship of SQL status on line 39
    #------------------------------------------------------------------------------
    
    sqlStatusSet = mbo.getMboSet("OKESQLSTATUS")
    sqlStatusMbo = sqlStatusSet.add(MboConstants.NOACCESSCHECK)
    sqlStatusMbo.setValue("SQLNUM", mbo.getString("SQLNUM"))
    sqlStatusMbo.setValue("STATUS", newStatus)
    sqlStatusMbo.setValue("MEMO", "placeholder")
    sqlStatusMbo.setValue("CHANGEBY", user)
    sqlStatusMbo.setValue("CHANGEDATE", newStatusDate)
    
    return
