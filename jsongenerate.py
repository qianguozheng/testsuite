# -*- coding: utf-8 -*-
"""
Generate more json format file for stress test.

Author: guozhengqian0825@126.com
"""
import json
#data1 = { "actions" : [ { "action" : "install", "fileName" : "缘分-同城单身男女交友约会必备神器.ipa", "packageName" : "", "resourceId" : "5349637215b2048f71ca76eeb0451f6169b5087a", "resultCode" : 0, "resultMessage" : "Success", "time" : "2015-08-19 16:36:49" } ], "brand" : "Apple Inc", "deviceId" : "047DC24000002AC6", "imei" : "352041064076720", "imsi" : "460008250386834", "logId" : "143997335369602", "macAddr" : "b8:09:8a:70:98:3f6", "model" : "iPhone6,2", "operator" : "9527", "serialNumber" : "EA1A20F54A36" }
data2 = json.loads('{ "actions" : [ { "action" : "install", "fileName" : "test.ipa", "packageName" : "", "resourceId" : "5349637215b2048f71ca76eeb0451f6169b5087a", "resultCode" : 0, "resultMessage" : "Success", "time" : "2015-08-19 16:36:49" } ], "brand" : "Apple Inc", "deviceId" : "047DC24000002AC6", "imei" : "352041064076720", "imsi" : "460008250386834", "logId" : "143997335369602", "macAddr" : "b8:09:8a:70:98:3f6", "model" : "iPhone6,2", "operator" : "9527", "serialNumber" : "EA1A20F54A36" }')

dataArr= data2["actions"]

dd = json.loads(json.dumps(dataArr[0], ensure_ascii=False))



fd = open("/home/weeds/journal-2015-08-20.log", 'w')

for i in range(1, 2000):
    i = i + 1;
    app = "%s%d" % ("hello you ", i)
    #dd["macAddr"] = app
    
    #toList = []
    #toList.append(dd)
    
    response = {}
    #response["actions"] = dict_to_list(dd)
    response["macAddr"] = app;
    response["actions"] = dataArr
    
    
    
    fd.write(json.dumps(response))
    fd.write('\n')
fd.close()


