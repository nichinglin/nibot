echo 'source /opt/ros/kinetic/setup.bash'
echo 'source ~/nibot/02_software/catkin_ws/devel/setup.bash'
echo 'virtualenv nibot/virtualenv/bin/activate'

source $HOME/nibot/virtualenv/bin/activate
source /opt/ros/kinetic/setup.bash
source $HOME/nibot/02_software/catkin_ws/devel/setup.bash

#PYTHONPATH=$HOME/nibot/virtualenv/bin/python

alias ws-make='ws-path; catkin_make -j8; cd -'
alias ws-path='cd $HOME/nibot/02_software/catkin_ws'
alias jupyter='jupyter notebook $HOME/nibot/'
