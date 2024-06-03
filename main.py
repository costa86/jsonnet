import subprocess
import json


source = """
local folderName = "myFolder";
local surname = "silva";
local Base = {a:1,b:self.a+1};
local obj = [i for i in std.range(1,10)];
local test = [Base];
local myFun(x,y) = x+y;
local createPerson(name, age) = {
    name: name,
    age: age
};

local hi = [i for i in obj];
local createHost(name, ip) = {
    customName: name,
    customIp: ip
};


{
  folderName: {
    name: folderName,
    welcome: "Hello " + surname,
    num: obj,
    TEST: myFun(10,20)
  },
  p1: createPerson("ana",5),
evens: {
      ['f' + x]: true
      for x in hi
    },
a: createHost("hello","124.0")
}
"""
output = subprocess.check_output(
    [
        "./hello",
        source,
    ]
)

data = json.loads(output)

print(data)
