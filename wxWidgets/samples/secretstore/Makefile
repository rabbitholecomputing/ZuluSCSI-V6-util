# =========================================================================
#     This makefile was generated by
#     Bakefile 0.2.13 (http://www.bakefile.org)
#     Do not modify, all changes will be overwritten!
# =========================================================================




prefix = /mingw64
exec_prefix = ${prefix}
datarootdir = ${prefix}/share
INSTALL = /usr/bin/install -c
EXEEXT = .exe
BK_DEPS = /home/gregc/Development/ZuluSCSI-V6-util/wxWidgets/bk-deps
srcdir = .
top_srcdir = ../..
LIBS = -lz -lrpcrt4 -loleaut32 -lole32 -luuid -lcurl -luxtheme -lwinspool -lwinmm -lshell32 -lshlwapi -lcomctl32 -lcomdlg32 -ladvapi32 -lversion -lws2_32 -lgdi32 -loleacc -lwinhttp
CXX = g++
CXXFLAGS = 
CPPFLAGS = 
LDFLAGS = 
WX_LIB_FLAVOUR = 
TOOLKIT = MSW
TOOLKIT_LOWERCASE = msw
TOOLKIT_VERSION = 
EXTRALIBS =    -lz -lrpcrt4 -loleaut32 -lole32 -luuid -lcurl -luxtheme -lwinspool -lwinmm -lshell32 -lshlwapi -lcomctl32 -lcomdlg32 -ladvapi32 -lversion -lws2_32 -lgdi32 -loleacc -lwinhttp -lpcre2-16 
EXTRALIBS_XML =  -lexpat
EXTRALIBS_GUI = -lpng -lz -ljpeg -ltiff -ljbig
WX_CPPFLAGS = -I${wx_top_builddir}/lib/wx/include/msw-unicode-3.3 -I${top_srcdir}/include -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE= 
WX_CXXFLAGS = -Wall -Wundef -Wunused-parameter -Wno-ctor-dtor-privacy -Woverloaded-virtual -O2 -IC:/tools/msys64/mingw64/include/webp -DLIBDEFLATE_DLL  
WX_LDFLAGS = 
HOST_SUFFIX = 
SAMPLES_RPATH_FLAG = 
SAMPLES_CXXFLAGS =  
wx_top_builddir = C:/tools/msys64/home/gregc/Development/ZuluSCSI-V6-util/wxWidgets

### Variables: ###

DESTDIR = 
WX_RELEASE = 3.3
LIBDIRNAME = $(wx_top_builddir)/lib
SECRETSTORE_CXXFLAGS = $(WX_CPPFLAGS) -D__WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p) \
	$(__DEBUG_DEFINE_p) $(__EXCEPTIONS_DEFINE_p) $(__RTTI_DEFINE_p) \
	$(__THREAD_DEFINE_p) -I$(srcdir) $(__DLLFLAG_p) -DwxUSE_GUI=0 $(WX_CXXFLAGS) \
	$(SAMPLES_CXXFLAGS) $(CPPFLAGS) $(CXXFLAGS)
SECRETSTORE_OBJECTS =  \
	secretstore_secretstore.o

### Conditionally set variables: ###

#CXXC = $(CXX)
CXXC = $(BK_DEPS) $(CXX)
#PORTNAME = base
PORTNAME = $(TOOLKIT_LOWERCASE)$(TOOLKIT_VERSION)
#WXBASEPORT = _carbon
#WXDEBUGFLAG = d
#WXUNIVNAME = univ
EXTRALIBS_FOR_BASE = $(EXTRALIBS)
#EXTRALIBS_FOR_BASE = $(EXTRALIBS) \
#	$(EXTRALIBS_XML) $(EXTRALIBS_GUI)
EXTRALIBS_FOR_GUI = $(EXTRALIBS_GUI)
#EXTRALIBS_FOR_GUI = 
#__WXUNIV_DEFINE_p = -D__WXUNIVERSAL__
#__DEBUG_DEFINE_p = -DwxDEBUG_LEVEL=0
#__EXCEPTIONS_DEFINE_p = -DwxNO_EXCEPTIONS
#__RTTI_DEFINE_p = -DwxNO_RTTI
#__THREAD_DEFINE_p = -DwxNO_THREADS
__DLLFLAG_p = -DWXUSINGDLL
COND_MONOLITHIC_0___WXLIB_BASE_p = \
	-lwx_base$(WXBASEPORT)u$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
__WXLIB_BASE_p = $(COND_MONOLITHIC_0___WXLIB_BASE_p)
COND_MONOLITHIC_1___WXLIB_MONO_p = \
	-lwx_$(PORTNAME)$(WXUNIVNAME)u$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__WXLIB_MONO_p = $(COND_MONOLITHIC_1___WXLIB_MONO_p)
#__LIB_SCINTILLA_IF_MONO_p \
#	= $(__LIB_SCINTILLA_p)
__LIB_SCINTILLA_p = \
	-lwxscintilla$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_LEXILLA_IF_MONO_p = $(__LIB_LEXILLA_p)
__LIB_LEXILLA_p = \
	-lwxlexilla$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_TIFF_p \
#	= \
#	-lwxtiff$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_JPEG_p \
#	= \
#	-lwxjpeg$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_PNG_p \
#	= \
#	-lwxpng$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_ZLIB_p = \
#	-lwxzlib$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_REGEX_p = \
#	-lwxregexu$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_EXPAT_p = \
#	-lwxexpat$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)

### Targets: ###

all: secretstore$(EXEEXT)

install: 

uninstall: 

install-strip: install

clean: 
	rm -rf ./.deps ./.pch
	rm -f ./*.o
	rm -f secretstore$(EXEEXT)

distclean: clean
	rm -f config.cache config.log config.status bk-deps bk-make-pch Makefile

secretstore$(EXEEXT): $(SECRETSTORE_OBJECTS)
	$(CXX) -o $@ $(SECRETSTORE_OBJECTS)    -L$(LIBDIRNAME)  $(SAMPLES_RPATH_FLAG)  $(LDFLAGS)  $(WX_LDFLAGS) $(__WXLIB_BASE_p)  $(__WXLIB_MONO_p) $(__LIB_SCINTILLA_IF_MONO_p) $(__LIB_LEXILLA_IF_MONO_p) $(__LIB_TIFF_p) $(__LIB_JPEG_p) $(__LIB_PNG_p)  $(EXTRALIBS_FOR_GUI) $(__LIB_ZLIB_p) $(__LIB_REGEX_p) $(__LIB_EXPAT_p) $(EXTRALIBS_FOR_BASE) $(LIBS)

secretstore_secretstore.o: $(srcdir)/secretstore.cpp
	$(CXXC) -c -o $@ $(SECRETSTORE_CXXFLAGS) $(srcdir)/secretstore.cpp


# Include dependency info, if present:
-include ./.deps/*.d

.PHONY: all install uninstall clean distclean
