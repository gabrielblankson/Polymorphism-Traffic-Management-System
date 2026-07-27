# Polymorphism – Traffic Management System

Demonstrates run-time polymorphism using method overriding.

A parent class `TrafficDevice` defines a common `activate()` interface.
Child classes (`TrafficLight`, `SpeedCamera`, `PedestrianSignal`, `EmergencySiren`)
each override `activate()` with their own behaviour. All devices are stored in a
list and activated through the same loop, without checking their type —
new device types (e.g. `EmergencySiren`) can be added without modifying
the activation loop.

## Run
```
python traffic_devices.py
```Author```
Blankson Gabriel
