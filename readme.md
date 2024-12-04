# Vehicular Automation Simulation Engine
### An Object-Oriented solution to self-driving cars

## Intro
V.A.S.E. is a dynamic, intelligent, self-correctional engine that simulates
how an autonomous car should behave.
The technology is simple, it loads a scene, makes decisions based on 
the elements in the scene, and takes decisions.
'decisions' refers to speed, braking, direction controls.


## Working
The program uses 2 classes
> Braking/Accelerating Locomotion Driver
>> Responsible for the speed, and stops

> Navigational Ingenuity Control Engine
>> Responsible for taking turns and changing directions

Other classes such as Persistence, SceneLoader etc. are core classes 
responsible for the working.

## Technology
Built with Python 3.11, The program uses the following module
(some which might require installation);

```text
colorama
pickle
json
random
```

