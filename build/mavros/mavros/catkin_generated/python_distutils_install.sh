#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/pi/propelled_cow/src/mavros/mavros"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/pi/propelled_cow/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/pi/propelled_cow/install/lib/python2.7/dist-packages:/home/pi/propelled_cow/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/pi/propelled_cow/build" \
    "/usr/bin/python" \
    "/home/pi/propelled_cow/src/mavros/mavros/setup.py" \
    build --build-base "/home/pi/propelled_cow/build/mavros/mavros" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/pi/propelled_cow/install" --install-scripts="/home/pi/propelled_cow/install/bin"
