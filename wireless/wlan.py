import numpy as np
#   @Author Pakin aka Mehhhehhe

#--------------------------------------------------------
# Formula
def BETA(frequency,free_space_distance): # Frequency in MHz, R in km
    return (32.45 + 20*np.log10(frequency*1000) + 20*np.log10(free_space_distance/1000))

def indoor_propagation(frequency,r,r0,n,waf,faf,p,q):
    Lp = BETA(frequency,r0) + 10*np.log10((r/r0)**n) + (p*waf) + (q*faf)
    return Lp

def indoor_propagationITU(transmit_power,r,waf,faf,p,q):
    receive_power = transmit_power - 41 - 31*np.log10(r) + (p*waf) + (q*faf)
    return receive_power

def powerRTL_NOGain(power_receive, power_transmit, path_loss):
    if power_receive is None:
        return (power_transmit - path_loss)
    elif power_transmit is None:
        return (power_receive + path_loss)
    
def powerRTL_Gain(power_receive, power_transmit, path_loss, transmit_gain, receive_gain):
    if power_receive is None:
        return (power_transmit - path_loss + transmit_gain + receive_gain)
    elif power_transmit is None:
        return (power_receive + path_loss - transmit_gain - receive_gain)

#--------------------------------------------------------
#   Call Function

# Find receiver power if both gain are unity. 
def FindReceiverPower(frequency,totalDistance,initSpace,lossExpo,wallMat,floorMat,powerTrans,wallNum,floorNum,senseSpec):
    print("\nFinding Beta ... \t\t\tResult : ",BETA(frequency,initSpace)," dB")
    if type(wallMat) == int or type(floorMat) == int:
        Lp = indoor_propagation(frequency,totalDistance,initSpace,path_loss_expo.get(lossExpo),wallMat,floorMat,wallNum,floorNum)
    else:
        Lp = indoor_propagation(frequency,totalDistance,initSpace,path_loss_expo.get(lossExpo),WAF2400.get(wallMat),WAF2400.get(floorMat),wallNum,floorNum)
    print("Finding Propagation Loss(Lp) ... \tResult: ",Lp," dB")
    Pr = powerRTL_NOGain(None,powerTrans,Lp)
    print("\nReceived Power = ",Pr," dBm")
    print("Can be used? : ",isInRange(Pr))
    if senseSpec is not None:
        print("Is under desired power: ",isMoreThan(Pr,senseSpec))

# Find a distance if signal strength equal to any.
def FindDistance(receivePower, transmitPower, initSpace, frequency, lossExpo, wallMat, floorMat, wallnum, floornum):
    if type(wallMat) == int or type(floorMat) == int:
        return (    # ERROR @ numpy.core. Avoid use!
            np.float_power((initSpace**lossExpo)*(10**((transmitPower-receivePower-BETA(frequency,initSpace)-(wallMat*wallnum)-(floorMat*floornum))/10)),1/lossExpo)
        )
    else:
        return (
            np.float_power((initSpace**path_loss_expo.get(lossExpo))*(10**((transmitPower-receivePower-BETA(frequency,initSpace)-(WAF2400.get(wallMat)*wallnum)-(WAF2400.get(floorMat)*floornum))/10)),1/path_loss_expo.get(lossExpo))
        )

def FindDistanceIndoor5G(receivePower, transmitPower, wallMat, floorMat, wallnum, floornum): # For 5G
    if wallMat is None and floorMat is None and wallnum is None and floornum is None:
        return (
            10**((transmitPower-receivePower-41)/31)
        )
    else:
        if type(wallMat) == int or type(floorMat) == int:
            return (
                10**((transmitPower-receivePower-41-(wallMat*wallnum)-(floorMat*floornum))/31)
            )
        else:
            return (
                10**((transmitPower-receivePower-41-(WAF2400.get(wallMat)*wallnum)-(WAF2400.get(floorMat)*floornum))/31)
            )
#--------------------------------------------------------
# Dictionary
WAF2400 = {
    "Foundation wall":15,
    "Brick":12,
    "Concrete":12,
    "Concrete block":12,
    "Elevator":10,
    "Metal":10,
    "Metal rack":6,
    "Drywall":3,
    "Sheetrock":3,
    "Glass":3,
    "Wood door":3,
    "Cubicle wall":2,
    "Plaster board_alter":6
}

path_loss_expo = {
    "Free space":2,
    "Flat rural":3,
    "Indoor building":3.1,
    "Rolling rural":3.5,
    "Suburban":4,
    "Urban":4.5
}
#-------------------------------------------------------
# Condition check
def isInRange(sensitivity): # dBm
    if sensitivity < -30 and sensitivity > -90:
        return "Usable"
def isMoreThan(currentSensitivity, Spec):
    if currentSensitivity > Spec:
        return "Yes"
    else:
        return "Too far! Bad quality"
#-------------------------------------------------------

#   Find power of receiver (signal strength)
#   Parameter : 
#   1. Frequency -> (2.4/5) GHz (Currently only test on 2.4G)
#   2. Total Distance from transmitter to receviver (ignore wall and floor)
#   3. Initial distance from transmitter to floor or wall
#   4. Path loss exponent (Check @ dictionary [path_loss_expo])
#   5. Wall Material (Check @ dictionary [WAF2400])
#   6. Floor Material (Check @ dictionary [WAF2400])
#   7. Transmitter Power (as dBm)
#   8. Number of wall
#   9. Number of floor
#   10. Desired signal strength (can be "None")
#  **** You can use 2.4GHz (Method will change to MHz later [auto])
#   Case 1 : With desired signal stength at -75 dBm
result = FindReceiverPower(2.4,35,5,"Indoor building","Drywall","Foundation wall",20,1,0,-75)
print()
#   Case 2 : No desired signal strength
result2 = FindReceiverPower(2.4,35,5,"Indoor building",6,0,20,1,0,None)
print("\n\n")
#   Find total distance with knowing receiver's power or signal strength
#   Parameter : 
#   1. Receiver's power / signal strength
#   2. Transmitter power
#   3. Initial distance to obstacle (wall/floor)
#   4. Frequency -> Support only 2.4G
#   5. Path Loss Exponent
#   6. Wall material
#   7. Floor Material
#   8. Number of wall
#   9. Number of floor
print(FindDistance(-66.2316,20,5,2.4,"Indoor building","Plaster board_alter","Foundation wall",1,0))
print(FindDistanceIndoor5G(-82,23,None,None,None,None))
print(FindDistanceIndoor5G(-82,23,"Plaster board_alter","Foundation wall",1,0))