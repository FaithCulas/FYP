INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_STREAM_BLOCKS Stream_Blocks)

FIND_PATH(
    STREAM_BLOCKS_INCLUDE_DIRS
    NAMES Stream_Blocks/api.h
    HINTS $ENV{STREAM_BLOCKS_DIR}/include
        ${PC_STREAM_BLOCKS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    STREAM_BLOCKS_LIBRARIES
    NAMES gnuradio-Stream_Blocks
    HINTS $ENV{STREAM_BLOCKS_DIR}/lib
        ${PC_STREAM_BLOCKS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/Stream_BlocksTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(STREAM_BLOCKS DEFAULT_MSG STREAM_BLOCKS_LIBRARIES STREAM_BLOCKS_INCLUDE_DIRS)
MARK_AS_ADVANCED(STREAM_BLOCKS_LIBRARIES STREAM_BLOCKS_INCLUDE_DIRS)
