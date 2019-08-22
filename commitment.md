### Aug 21
* It's really hard to read tornado framework code, it just stucks right at the start() method of IOLoop 

### Aug 22
* OMG, since IOLoop is a subclass of Configurable so it is initialized by initialize() method __(Not \_\_init\_\_() method)__
* After going around in the __ioloop.py__ file, I found out that in configure() method, in which importing the BaseIOLoop which basically contains all the code that I wanna inspect
* But still, I'm still trying to figure out why the __configure()__ method is called, maybe somewhere else but not in this __ioloop.py__ file 