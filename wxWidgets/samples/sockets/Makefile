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
WINDRES = windres
NM = nm
BK_DEPS = /home/gregc/Development/ZuluSCSI-V6-util/wxWidgets/bk-deps
srcdir = .
top_srcdir = ../..
LIBS = -lz -lrpcrt4 -loleaut32 -lole32 -luuid -lcurl -luxtheme -lwinspool -lwinmm -lshell32 -lshlwapi -lcomctl32 -lcomdlg32 -ladvapi32 -lversion -lws2_32 -lgdi32 -loleacc -lwinhttp
LDFLAGS_GUI = -mwindows
CXX = g++
CXXFLAGS = 
CPPFLAGS = 
LDFLAGS = 
USE_DPI_AWARE_MANIFEST = 2
WX_LIB_FLAVOUR = 
TOOLKIT = MSW
TOOLKIT_LOWERCASE = msw
TOOLKIT_VERSION = 
TOOLCHAIN_FULLNAME = msw-unicode-3.3
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
WX_VERSION = $(WX_RELEASE).0
LIBDIRNAME = $(wx_top_builddir)/lib
CLIENT_CXXFLAGS = $(WX_CPPFLAGS) -D__WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p) \
	$(__DEBUG_DEFINE_p) $(__EXCEPTIONS_DEFINE_p) $(__RTTI_DEFINE_p) \
	$(__THREAD_DEFINE_p) -I$(srcdir) $(__DLLFLAG_p) -I$(srcdir)/../../samples \
	$(WX_CXXFLAGS) $(SAMPLES_CXXFLAGS) $(CPPFLAGS) $(CXXFLAGS)
CLIENT_OBJECTS =  \
	$(__client___win32rc) \
	client_client.o
SERVER_CXXFLAGS = $(WX_CPPFLAGS) -D__WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p) \
	$(__DEBUG_DEFINE_p) $(__EXCEPTIONS_DEFINE_p) $(__RTTI_DEFINE_p) \
	$(__THREAD_DEFINE_p) -I$(srcdir) $(__DLLFLAG_p) -I$(srcdir)/../../samples \
	$(WX_CXXFLAGS) $(SAMPLES_CXXFLAGS) $(CPPFLAGS) $(CXXFLAGS)
SERVER_OBJECTS =  \
	$(__server___win32rc) \
	server_server.o
BASECLIENT_CXXFLAGS = $(WX_CPPFLAGS) -D__WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p) \
	$(__DEBUG_DEFINE_p) $(__EXCEPTIONS_DEFINE_p) $(__RTTI_DEFINE_p) \
	$(__THREAD_DEFINE_p) -I$(srcdir) $(__DLLFLAG_p) -DwxUSE_GUI=0 $(WX_CXXFLAGS) \
	$(SAMPLES_CXXFLAGS) $(CPPFLAGS) $(CXXFLAGS)
BASECLIENT_OBJECTS =  \
	baseclient_baseclient.o
BASESERVER_CXXFLAGS = $(WX_CPPFLAGS) -D__WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p) \
	$(__DEBUG_DEFINE_p) $(__EXCEPTIONS_DEFINE_p) $(__RTTI_DEFINE_p) \
	$(__THREAD_DEFINE_p) -I$(srcdir) $(__DLLFLAG_p) -DwxUSE_GUI=0 $(WX_CXXFLAGS) \
	$(SAMPLES_CXXFLAGS) $(CPPFLAGS) $(CXXFLAGS)
BASESERVER_OBJECTS =  \
	baseserver_baseserver.o

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
__client___depname = client$(EXEEXT)
COND_PLATFORM_OS2_1___client___os2_emxbindcmd = $(NM) client$(EXEEXT) | if grep \
	-q pmwin.763 ; then emxbind -ep client$(EXEEXT) ; fi
#__client___os2_emxbindcmd = $(COND_PLATFORM_OS2_1___client___os2_emxbindcmd)
__client___win32rc = client_sample_rc.o
#__client_app_Contents_PkgInfo___depname \
#	= client.app/Contents/PkgInfo
#__client_bundle___depname = client_bundle
#____client_BUNDLE_TGT_REF_DEP = \
#	$(__client_app_Contents_PkgInfo___depname)
#____client_BUNDLE_TGT_REF_DEP = \
#	$(__client_app_Contents_PkgInfo___depname)
#____client_BUNDLE_TGT_REF_DEP \
#	= $(__client_app_Contents_PkgInfo___depname)
#____client_BUNDLE_TGT_REF_DEP \
#	= $(__client_app_Contents_PkgInfo___depname)
#____client_BUNDLE_TGT_REF_DEP \
#	= $(__client_app_Contents_PkgInfo___depname)
#__LIB_SCINTILLA_IF_MONO_p \
#	= $(__LIB_SCINTILLA_p)
#__LIB_LEXILLA_IF_MONO_p = $(__LIB_LEXILLA_p)
__server___depname = server$(EXEEXT)
COND_PLATFORM_OS2_1___server___os2_emxbindcmd = $(NM) server$(EXEEXT) | if grep \
	-q pmwin.763 ; then emxbind -ep server$(EXEEXT) ; fi
#__server___os2_emxbindcmd = $(COND_PLATFORM_OS2_1___server___os2_emxbindcmd)
__server___win32rc = server_sample_rc.o
#__server_app_Contents_PkgInfo___depname \
#	= server.app/Contents/PkgInfo
#__server_bundle___depname = server_bundle
#____server_BUNDLE_TGT_REF_DEP = \
#	$(__server_app_Contents_PkgInfo___depname)
#____server_BUNDLE_TGT_REF_DEP = \
#	$(__server_app_Contents_PkgInfo___depname)
#____server_BUNDLE_TGT_REF_DEP \
#	= $(__server_app_Contents_PkgInfo___depname)
#____server_BUNDLE_TGT_REF_DEP \
#	= $(__server_app_Contents_PkgInfo___depname)
#____server_BUNDLE_TGT_REF_DEP \
#	= $(__server_app_Contents_PkgInfo___depname)
#__LIB_SCINTILLA_IF_MONO_p_1 \
#	= $(__LIB_SCINTILLA_p)
#__LIB_LEXILLA_IF_MONO_p_1 = $(__LIB_LEXILLA_p)
#__LIB_PNG_IF_MONO_p = $(__LIB_PNG_p)
#__LIB_PNG_IF_MONO_p_1 = $(__LIB_PNG_p)
#__WXUNIV_DEFINE_p_0 = --define __WXUNIVERSAL__
#__DEBUG_DEFINE_p_0 = --define wxDEBUG_LEVEL=0
#__EXCEPTIONS_DEFINE_p_0 = --define wxNO_EXCEPTIONS
#__RTTI_DEFINE_p_0 = --define wxNO_RTTI
#__THREAD_DEFINE_p_0 = --define wxNO_THREADS
__DLLFLAG_p_0 = --define WXUSINGDLL
__WIN32_DPI_MANIFEST_p = \
	--define \
	wxUSE_DPI_AWARE_MANIFEST=$(USE_DPI_AWARE_MANIFEST)
__RCDEFDIR_p = --include-dir \
	$(LIBDIRNAME)/wx/include/$(TOOLCHAIN_FULLNAME)
COND_MONOLITHIC_0___WXLIB_CORE_p = \
	-lwx_$(PORTNAME)$(WXUNIVNAME)u$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)_core-$(WX_RELEASE)$(HOST_SUFFIX)
__WXLIB_CORE_p = $(COND_MONOLITHIC_0___WXLIB_CORE_p)
__LIB_SCINTILLA_p = \
	-lwxscintilla$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
__LIB_LEXILLA_p = \
	-lwxlexilla$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_TIFF_p \
#	= \
#	-lwxtiff$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__LIB_JPEG_p \
#	= \
#	-lwxjpeg$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__WXUNIV_DEFINE_p = -D__WXUNIVERSAL__
#__DEBUG_DEFINE_p = -DwxDEBUG_LEVEL=0
#__EXCEPTIONS_DEFINE_p = -DwxNO_EXCEPTIONS
#__RTTI_DEFINE_p = -DwxNO_RTTI
#__THREAD_DEFINE_p = -DwxNO_THREADS
__DLLFLAG_p = -DWXUSINGDLL
COND_MONOLITHIC_0___WXLIB_NET_p = \
	-lwx_base$(WXBASEPORT)u$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)_net-$(WX_RELEASE)$(HOST_SUFFIX)
__WXLIB_NET_p = $(COND_MONOLITHIC_0___WXLIB_NET_p)
COND_MONOLITHIC_0___WXLIB_BASE_p = \
	-lwx_base$(WXBASEPORT)u$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
__WXLIB_BASE_p = $(COND_MONOLITHIC_0___WXLIB_BASE_p)
COND_MONOLITHIC_1___WXLIB_MONO_p = \
	-lwx_$(PORTNAME)$(WXUNIVNAME)u$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)-$(WX_RELEASE)$(HOST_SUFFIX)
#__WXLIB_MONO_p = $(COND_MONOLITHIC_1___WXLIB_MONO_p)
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

all: $(__client___depname) $(__client_bundle___depname) $(__server___depname) $(__server_bundle___depname) baseclient$(EXEEXT) baseserver$(EXEEXT)

install: 

uninstall: 

install-strip: install

clean: 
	rm -rf ./.deps ./.pch
	rm -f ./*.o
	rm -f client$(EXEEXT)
	rm -rf client.app
	rm -f server$(EXEEXT)
	rm -rf server.app
	rm -f baseclient$(EXEEXT)
	rm -f baseserver$(EXEEXT)

distclean: clean
	rm -f config.cache config.log config.status bk-deps bk-make-pch Makefile

client$(EXEEXT): $(CLIENT_OBJECTS) $(__client___win32rc)
	$(CXX) -o $@ $(CLIENT_OBJECTS)    -L$(LIBDIRNAME)  $(LDFLAGS_GUI) $(SAMPLES_RPATH_FLAG)    $(LDFLAGS)  $(WX_LDFLAGS) $(__WXLIB_CORE_p)  $(__WXLIB_NET_p)  $(__WXLIB_BASE_p)  $(__WXLIB_MONO_p) $(__LIB_SCINTILLA_IF_MONO_p) $(__LIB_LEXILLA_IF_MONO_p) $(__LIB_TIFF_p) $(__LIB_JPEG_p) $(__LIB_PNG_p)  $(EXTRALIBS_FOR_GUI) $(__LIB_ZLIB_p) $(__LIB_REGEX_p) $(__LIB_EXPAT_p) $(EXTRALIBS_FOR_BASE) $(LIBS)
	$(__client___os2_emxbindcmd)

#client.app/Contents/PkgInfo: $(__client___depname) $(top_srcdir)/src/osx/carbon/Info.plist.in $(top_srcdir)/src/osx/carbon/wxmac.icns
#	mkdir -p client.app/Contents
#	mkdir -p client.app/Contents/MacOS
#	mkdir -p client.app/Contents/Resources
#	
#	
#	sed -e "s/\$${MACOSX_BUNDLE_GUI_IDENTIFIER}/org.wxwidgets.client/" \
#	-e "s/\$${MACOSX_BUNDLE_EXECUTABLE_NAME}/client/" \
#	-e "s/\$${MACOSX_BUNDLE_BUNDLE_NAME}/client/" \
#	-e "s/\$${MACOSX_BUNDLE_COPYRIGHT}/Copyright 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_BUNDLE_VERSION}/$(WX_VERSION)/" \
#	-e "s/\$${MACOSX_BUNDLE_INFO_STRING}/client version $(WX_VERSION), (c) 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_LONG_VERSION_STRING}/$(WX_VERSION), (c) 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_SHORT_VERSION_STRING}/$(WX_RELEASE)/" \
#	$(top_srcdir)/src/osx/carbon/Info.plist.in >client.app/Contents/Info.plist
#	
#	
#	/bin/echo "APPL????" >client.app/Contents/PkgInfo
#	
#	
#	ln -f client$(EXEEXT) client.app/Contents/MacOS/client
#	
#	
#	cp -f $(top_srcdir)/src/osx/carbon/wxmac.icns client.app/Contents/Resources/wxmac.icns

#client_bundle: $(____client_BUNDLE_TGT_REF_DEP)

server$(EXEEXT): $(SERVER_OBJECTS) $(__server___win32rc)
	$(CXX) -o $@ $(SERVER_OBJECTS)    -L$(LIBDIRNAME)  $(LDFLAGS_GUI) $(SAMPLES_RPATH_FLAG)    $(LDFLAGS)  $(WX_LDFLAGS) $(__WXLIB_CORE_p)  $(__WXLIB_NET_p)  $(__WXLIB_BASE_p)  $(__WXLIB_MONO_p) $(__LIB_SCINTILLA_IF_MONO_p_1) $(__LIB_LEXILLA_IF_MONO_p_1) $(__LIB_TIFF_p) $(__LIB_JPEG_p) $(__LIB_PNG_p)  $(EXTRALIBS_FOR_GUI) $(__LIB_ZLIB_p) $(__LIB_REGEX_p) $(__LIB_EXPAT_p) $(EXTRALIBS_FOR_BASE) $(LIBS)
	$(__server___os2_emxbindcmd)

#server.app/Contents/PkgInfo: $(__server___depname) $(top_srcdir)/src/osx/carbon/Info.plist.in $(top_srcdir)/src/osx/carbon/wxmac.icns
#	mkdir -p server.app/Contents
#	mkdir -p server.app/Contents/MacOS
#	mkdir -p server.app/Contents/Resources
#	
#	
#	sed -e "s/\$${MACOSX_BUNDLE_GUI_IDENTIFIER}/org.wxwidgets.server/" \
#	-e "s/\$${MACOSX_BUNDLE_EXECUTABLE_NAME}/server/" \
#	-e "s/\$${MACOSX_BUNDLE_BUNDLE_NAME}/server/" \
#	-e "s/\$${MACOSX_BUNDLE_COPYRIGHT}/Copyright 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_BUNDLE_VERSION}/$(WX_VERSION)/" \
#	-e "s/\$${MACOSX_BUNDLE_INFO_STRING}/server version $(WX_VERSION), (c) 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_LONG_VERSION_STRING}/$(WX_VERSION), (c) 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_SHORT_VERSION_STRING}/$(WX_RELEASE)/" \
#	$(top_srcdir)/src/osx/carbon/Info.plist.in >server.app/Contents/Info.plist
#	
#	
#	/bin/echo "APPL????" >server.app/Contents/PkgInfo
#	
#	
#	ln -f server$(EXEEXT) server.app/Contents/MacOS/server
#	
#	
#	cp -f $(top_srcdir)/src/osx/carbon/wxmac.icns server.app/Contents/Resources/wxmac.icns

#server_bundle: $(____server_BUNDLE_TGT_REF_DEP)

baseclient$(EXEEXT): $(BASECLIENT_OBJECTS)
	$(CXX) -o $@ $(BASECLIENT_OBJECTS)    -L$(LIBDIRNAME)  $(SAMPLES_RPATH_FLAG)   $(LDFLAGS)  $(WX_LDFLAGS) $(__WXLIB_NET_p)  $(__WXLIB_BASE_p)  $(__WXLIB_MONO_p) $(__LIB_PNG_IF_MONO_p) $(__LIB_ZLIB_p) $(__LIB_REGEX_p) $(__LIB_EXPAT_p) $(EXTRALIBS_FOR_BASE) $(LIBS)

baseserver$(EXEEXT): $(BASESERVER_OBJECTS)
	$(CXX) -o $@ $(BASESERVER_OBJECTS)    -L$(LIBDIRNAME)  $(SAMPLES_RPATH_FLAG)   $(LDFLAGS)  $(WX_LDFLAGS) $(__WXLIB_NET_p)  $(__WXLIB_BASE_p)  $(__WXLIB_MONO_p) $(__LIB_PNG_IF_MONO_p_1) $(__LIB_ZLIB_p) $(__LIB_REGEX_p) $(__LIB_EXPAT_p) $(EXTRALIBS_FOR_BASE) $(LIBS)

client_sample_rc.o: $(srcdir)/../../samples/sample.rc
	$(WINDRES) -i$< -o$@    --define __WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p_0) $(__DEBUG_DEFINE_p_0)  $(__EXCEPTIONS_DEFINE_p_0) $(__RTTI_DEFINE_p_0) $(__THREAD_DEFINE_p_0) --include-dir $(srcdir) $(__DLLFLAG_p_0) $(__WIN32_DPI_MANIFEST_p) --include-dir $(srcdir)/../../samples $(__RCDEFDIR_p) --include-dir $(top_srcdir)/include

client_client.o: $(srcdir)/client.cpp
	$(CXXC) -c -o $@ $(CLIENT_CXXFLAGS) $(srcdir)/client.cpp

server_sample_rc.o: $(srcdir)/../../samples/sample.rc
	$(WINDRES) -i$< -o$@    --define __WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p_0) $(__DEBUG_DEFINE_p_0)  $(__EXCEPTIONS_DEFINE_p_0) $(__RTTI_DEFINE_p_0) $(__THREAD_DEFINE_p_0) --include-dir $(srcdir) $(__DLLFLAG_p_0) $(__WIN32_DPI_MANIFEST_p) --include-dir $(srcdir)/../../samples $(__RCDEFDIR_p) --include-dir $(top_srcdir)/include

server_server.o: $(srcdir)/server.cpp
	$(CXXC) -c -o $@ $(SERVER_CXXFLAGS) $(srcdir)/server.cpp

baseclient_baseclient.o: $(srcdir)/baseclient.cpp
	$(CXXC) -c -o $@ $(BASECLIENT_CXXFLAGS) $(srcdir)/baseclient.cpp

baseserver_baseserver.o: $(srcdir)/baseserver.cpp
	$(CXXC) -c -o $@ $(BASESERVER_CXXFLAGS) $(srcdir)/baseserver.cpp


# Include dependency info, if present:
-include ./.deps/*.d

.PHONY: all install uninstall clean distclean client_bundle server_bundle
