#
# CMakeLists.txt for libzypp-bindings/swig
#
#

ENABLE_TESTING()

SET( SWIG_INPUT "${CMAKE_CURRENT_SOURCE_DIR}/zypp.i" )

#
# Allow to build only a subset of language bindings via options
#

OPTION(BUILD_RUBY_BINDINGS "Build Ruby bindings" ON)
OPTION(BUILD_PYTHON_BINDINGS "Build Python bindings" ON)
OPTION(BUILD_PERL5_BINDINGS "Build Perl 5 bindings" ON)

#
# Let's see which target languages are available
#

IF(BUILD_RUBY_BINDINGS)
  FIND_PACKAGE(Ruby)
  IF(RUBY_LIBRARY AND RUBY_INCLUDE_PATH)
    ADD_SUBDIRECTORY(ruby)
  ENDIF()
ENDIF()

IF(BUILD_PYTHON_BINDINGS)
  # Enforce Python 3.8
  set(PythonLibs_FIND_VERSION 3.8)
  set(PythonLibs_FIND_VERSION_MAJOR 3)
  FIND_PACKAGE(PythonLibs)
  IF(PYTHON_LIBRARY)
    ADD_SUBDIRECTORY(python)
  ENDIF()
ENDIF()

IF(BUILD_PERL5_BINDINGS)
  FIND_PACKAGE(Perl)
  IF(PERL_EXECUTABLE)
    ADD_SUBDIRECTORY(perl5)
  ENDIF()
ENDIF()
