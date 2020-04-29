##
# CMakeLists.txt for libzypp-bindings/swig/python/tests
#

ENABLE_TESTING()

ADD_TEST(bindings_python_loading     python3 ${CMAKE_CURRENT_SOURCE_DIR}/loading.py)
ADD_TEST(bindings_python_repoinfo    python3 ${CMAKE_CURRENT_SOURCE_DIR}/repoinfo.py)
# FIXME: ResObject::constPtr* destructor handling causes a memory leak and a segfault
# when unloading zypp:
# Emitting removal of  <Swig Object of type 'zypp::ResObject::constPtr *' at 0xf6c88620>
# swig/python detected a memory leak of type 'zypp::ResObject::constPtr *', no destructor found.
# ADD_TEST(bindings_python_commit_callbacks  python3 ${CMAKE_CURRENT_SOURCE_DIR}/commit_callbacks.py)
# ADD_TEST(bindings_python_problems    python ${CMAKE_CURRENT_SOURCE_DIR}/problems.py)
# ADD_TEST(bindings_python_installed_path    python ${CMAKE_CURRENT_SOURCE_DIR}/installed_path.py)
