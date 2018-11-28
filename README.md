# README

RL Course project, CS6700.

_Authors: Aravinth Muthu, Varun Sundar_

## Dependencies

* [AirSim](https://github.com/Microsoft/AirSim)
* [CARLA](https://github.com/carla-simulator/carla)
* RL-Coach: You can use the version with this repository. We have significantly altered [coach](https://github.com/NervanaSystems/coach/blob/master/rl_coach/presets/CARLA_CIL.py) to suit our dependency needs.
* Keras-RL
* Tensorflow 1.12+
* CUDA 10.0, CUDNN 7.0.3
* Python 3.5

We have included a pip wheel in the binary directory for tensorflow.

## Building AirSim and CARLA

In case you are testing on Windows, you can build Unreal Engine as usual or download the available binaries. (version 4.19)

For Linux, you would be required to build Unreal Engine.To Do this:

1. Make sure you are [registered with Epic Games](https://docs.unrealengine.com/latest/INT/Platforms/Linux/BeginnerLinuxDeveloper/SettingUpAnUnrealWorkflow/1/index.html). This is required to get source code access for Unreal Engine.
2. Clone Unreal in your favorite folder and build it (this may take a while!). **Note**: We only support Unreal 4.18 at present.
   ```bash
   # go to the folder where you clone GitHub projects
   git clone -b 4.18 https://github.com/EpicGames/UnrealEngine.git
   cd UnrealEngine
   ./Setup.sh
   ./GenerateProjectFiles.sh
   make
   ```

Post this, you can build AirSim and Carla as usual. You could also cross-compile UE or use a dockefile (preferred) to get past this.

## Docker Containers

A much more hassle free process is to use the docker containers for each.

We have included our build files for this. 

First download Unreal Engine, AirSim and CARLA repositories into the base folder of this repository (see links above).

Run as:

```
docker build -t rl-project/simulators Dockerfiles
```

Execute the required binaries as:

```
docker run -p 2000-2002:2000-2002 --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 rl-project/simulators
```

If you wish to run only CARLA with docker, run:

```
docker run -p 2000-2002:2000-2002 --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 carlasim/carla:0.8.2
```

Swarm support documentation will be updated soon.

## Using the Presets

Run as:

```
coach -r -p <preset>
```

We have added additional presets for experimentation. These may be found at `coach-presets`.

## A3C on CARLA

Run 

```
coach -r -p CARLA_A3C
```

after having copied the preset `CARLA_A3C.py` into `coach/rl_coach`.

## D-DQN on AirSim

You can either train the network yourself or load the exciting weights by setting Train to True or False. 
Note: When you cancel the training, weights are saved and will overright the already trained weights (see `bin/Trained_Weights`).

### State:
We are taking as state input a depth image extended by the encoded information of the relative goal direction. 

### Action:
For this environment, we force the quadcopter to move in a fix plane and therefore confront the obstacles. The action space consist of three discrete actions and are available at any state:
- straight: Move in direction of current heading with 4m/s for 1s
- right yaw: Rotate right with 30°/s for 1s
- left yaw: Rotate left with 30°/s for 1s

## Imitation learning on AirSim

### Driving
Download data from: [link](https://aka.ms/AirSimTutorialDataset)

In `
Run `DataExplorationAndPreparation.py` and `TrainModel.py`.

Run `TestModel.py` with AirSim running in the background.  
