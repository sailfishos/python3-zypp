#
# CMakeLists.txt for libzypp-bindings/swig
#
#

ENABLE_TESTING()

SET( SWIG_INPUT "${CMAKE_CURRENT_SOURCE_DIR}/zypp.i" )

# Enforce Python 3.8
set(PythonLibs_FIND_VERSION 3.8)
set(PythonLibs_FIND_VERSION_MAJOR 3)
FIND_PACKAGE(PythonLibs)
IF(PYTHON_LIBRARY)
ADD_SUBDIRECTORY(python)
ENDIF()
