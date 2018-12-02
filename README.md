# nibot

# nibot
object recognition using dex-net

## How to setup
``` 
sudo apt-get install virtualenv
sudo apt-get install python-dev python-pip

cd ~/nibot
virtualenv -p /usr/bin/python2.7 virtualenv
pip list
source ~/nibot/environment.sh

pip install -r ~/nibot/requirements.txt
```

## catkin_make

```
cd ~/nibot
source environment.sh
cd ~/nibot/02_software/catkin_ws
catkin_make
```

## How to run

```
cd ~/nibot
source environment.sh
```

## Error List

#### `autolab-perception 0.0.4 has requirement ipython==5.5.0, but you'll have ipython 5.7.0 which is incompatible`

```
pip install ipython==5.5.0
pip install ~/nibot/catkin_ws/src/gqcnn
```

#### ` Make sure that you have installed "catkin_pkg", it is up to date and on the PYTHONPATH. `

` pip install catkin_pkg `

#### `ImportError: No module named em`

` pip install empy `
 

