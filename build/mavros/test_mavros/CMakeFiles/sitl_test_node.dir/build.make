# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/propelled_cow/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/propelled_cow/build

# Include any dependencies generated for this target.
include mavros/test_mavros/CMakeFiles/sitl_test_node.dir/depend.make

# Include the progress variables for this target.
include mavros/test_mavros/CMakeFiles/sitl_test_node.dir/progress.make

# Include the compile flags for this target's objects.
include mavros/test_mavros/CMakeFiles/sitl_test_node.dir/flags.make

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o: mavros/test_mavros/CMakeFiles/sitl_test_node.dir/flags.make
mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o: /home/pi/propelled_cow/src/mavros/test_mavros/sitl_test/sitl_test_node.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/propelled_cow/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o"
	cd /home/pi/propelled_cow/build/mavros/test_mavros && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o -c /home/pi/propelled_cow/src/mavros/test_mavros/sitl_test/sitl_test_node.cpp

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.i"
	cd /home/pi/propelled_cow/build/mavros/test_mavros && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pi/propelled_cow/src/mavros/test_mavros/sitl_test/sitl_test_node.cpp > CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.i

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.s"
	cd /home/pi/propelled_cow/build/mavros/test_mavros && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pi/propelled_cow/src/mavros/test_mavros/sitl_test/sitl_test_node.cpp -o CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.s

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.requires:

.PHONY : mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.requires

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.provides: mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.requires
	$(MAKE) -f mavros/test_mavros/CMakeFiles/sitl_test_node.dir/build.make mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.provides.build
.PHONY : mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.provides

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.provides.build: mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o


# Object files for target sitl_test_node
sitl_test_node_OBJECTS = \
"CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o"

# External object files for target sitl_test_node
sitl_test_node_EXTERNAL_OBJECTS =

/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: mavros/test_mavros/CMakeFiles/sitl_test_node.dir/build.make
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /home/pi/propelled_cow/devel/lib/libmavros_sitl_test.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /home/pi/propelled_cow/devel/lib/libmavros.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/librosconsole_bridge.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libGeographic.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libtinyxml2.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libclass_loader.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/libPocoFoundation.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libdl.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libroslib.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/librospack.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libpython2.7.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_program_options.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /home/pi/propelled_cow/devel/lib/libmavconn.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libtf2_ros.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libactionlib.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libmessage_filters.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libtf2.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libeigen_conversions.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/liborocos-kdl.so.1.3.0
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libcontrol_toolbox.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libtinyxml.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libdynamic_reconfigure_config_init_mutex.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/librealtime_tools.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libroscpp.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_filesystem.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_signals.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/librosconsole.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/liblog4cxx.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_regex.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/librostime.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /opt/ros/kinetic/lib/libcpp_common.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_system.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_thread.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_chrono.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_date_time.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libboost_atomic.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libpthread.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: /usr/lib/arm-linux-gnueabihf/libconsole_bridge.so
/home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node: mavros/test_mavros/CMakeFiles/sitl_test_node.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/propelled_cow/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node"
	cd /home/pi/propelled_cow/build/mavros/test_mavros && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sitl_test_node.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
mavros/test_mavros/CMakeFiles/sitl_test_node.dir/build: /home/pi/propelled_cow/devel/lib/test_mavros/sitl_test_node

.PHONY : mavros/test_mavros/CMakeFiles/sitl_test_node.dir/build

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/requires: mavros/test_mavros/CMakeFiles/sitl_test_node.dir/sitl_test/sitl_test_node.cpp.o.requires

.PHONY : mavros/test_mavros/CMakeFiles/sitl_test_node.dir/requires

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/clean:
	cd /home/pi/propelled_cow/build/mavros/test_mavros && $(CMAKE_COMMAND) -P CMakeFiles/sitl_test_node.dir/cmake_clean.cmake
.PHONY : mavros/test_mavros/CMakeFiles/sitl_test_node.dir/clean

mavros/test_mavros/CMakeFiles/sitl_test_node.dir/depend:
	cd /home/pi/propelled_cow/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/propelled_cow/src /home/pi/propelled_cow/src/mavros/test_mavros /home/pi/propelled_cow/build /home/pi/propelled_cow/build/mavros/test_mavros /home/pi/propelled_cow/build/mavros/test_mavros/CMakeFiles/sitl_test_node.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : mavros/test_mavros/CMakeFiles/sitl_test_node.dir/depend

