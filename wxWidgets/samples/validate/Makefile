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
VALIDATE_CXXFLAGS = $(WX_CPPFLAGS) -D__WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p) \
	$(__DEBUG_DEFINE_p) $(__EXCEPTIONS_DEFINE_p) $(__RTTI_DEFINE_p) \
	$(__THREAD_DEFINE_p) -I$(srcdir) $(__DLLFLAG_p) -I$(srcdir)/../../samples \
	$(WX_CXXFLAGS) $(SAMPLES_CXXFLAGS) $(CPPFLAGS) $(CXXFLAGS)
VALIDATE_OBJECTS =  \
	$(__validate___win32rc) \
	validate_validate.o

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
#__WXUNIV_DEFINE_p_1 = --define __WXUNIVERSAL__
#__DEBUG_DEFINE_p = -DwxDEBUG_LEVEL=0
#__DEBUG_DEFINE_p_1 = --define wxDEBUG_LEVEL=0
#__EXCEPTIONS_DEFINE_p = -DwxNO_EXCEPTIONS
#__EXCEPTIONS_DEFINE_p_1 = --define wxNO_EXCEPTIONS
#__RTTI_DEFINE_p = -DwxNO_RTTI
#__RTTI_DEFINE_p_1 = --define wxNO_RTTI
#__THREAD_DEFINE_p = -DwxNO_THREADS
#__THREAD_DEFINE_p_1 = --define wxNO_THREADS
__DLLFLAG_p = -DWXUSINGDLL
__DLLFLAG_p_1 = --define WXUSINGDLL
__WIN32_DPI_MANIFEST_p = \
	--define \
	wxUSE_DPI_AWARE_MANIFEST=$(USE_DPI_AWARE_MANIFEST)
COND_PLATFORM_OS2_1___validate___os2_emxbindcmd = $(NM) validate$(EXEEXT) | if \
	grep -q pmwin.763 ; then emxbind -ep validate$(EXEEXT) ; fi
#__validate___os2_emxbindcmd = $(COND_PLATFORM_OS2_1___validate___os2_emxbindcmd)
__RCDEFDIR_p = --include-dir \
	$(LIBDIRNAME)/wx/include/$(TOOLCHAIN_FULLNAME)
__validate___win32rc = validate_sample_rc.o
#__validate_app_Contents_PkgInfo___depname \
#	= validate.app/Contents/PkgInfo
#__validate_bundle___depname = validate_bundle
#____validate_BUNDLE_TGT_REF_DEP = \
#	$(__validate_app_Contents_PkgInfo___depname)
#____validate_BUNDLE_TGT_REF_DEP \
#	= $(__validate_app_Contents_PkgInfo___depname)
#____validate_BUNDLE_TGT_REF_DEP \
#	= $(__validate_app_Contents_PkgInfo___depname)
#____validate_BUNDLE_TGT_REF_DEP \
#	= $(__validate_app_Contents_PkgInfo___depname)
#____validate_BUNDLE_TGT_REF_DEP = \
#	$(__validate_app_Contents_PkgInfo___depname)
COND_MONOLITHIC_0___WXLIB_CORE_p = \
	-lwx_$(PORTNAME)$(WXUNIVNAME)u$(WXDEBUGFLAG)$(WX_LIB_FLAVOUR)_core-$(WX_RELEASE)$(HOST_SUFFIX)
__WXLIB_CORE_p = $(COND_MONOLITHIC_0___WXLIB_CORE_p)
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

all: validate$(EXEEXT) $(__validate_bundle___depname)

install: 

uninstall: 

install-strip: install

clean: 
	rm -rf ./.deps ./.pch
	rm -f ./*.o
	rm -f validate$(EXEEXT)
	rm -rf validate.app

distclean: clean
	rm -f config.cache config.log config.status bk-deps bk-make-pch Makefile

validate$(EXEEXT): $(VALIDATE_OBJECTS) $(__validate___win32rc)
	$(CXX) -o $@ $(VALIDATE_OBJECTS)    -L$(LIBDIRNAME)  $(LDFLAGS_GUI) $(SAMPLES_RPATH_FLAG)   $(LDFLAGS)  $(WX_LDFLAGS) $(__WXLIB_CORE_p)  $(__WXLIB_BASE_p)  $(__WXLIB_MONO_p) $(__LIB_SCINTILLA_IF_MONO_p) $(__LIB_LEXILLA_IF_MONO_p) $(__LIB_TIFF_p) $(__LIB_JPEG_p) $(__LIB_PNG_p)  $(EXTRALIBS_FOR_GUI) $(__LIB_ZLIB_p) $(__LIB_REGEX_p) $(__LIB_EXPAT_p) $(EXTRALIBS_FOR_BASE) $(LIBS)
	$(__validate___os2_emxbindcmd)

#validate.app/Contents/PkgInfo: validate$(EXEEXT) $(top_srcdir)/src/osx/carbon/Info.plist.in $(top_srcdir)/src/osx/carbon/wxmac.icns
#	mkdir -p validate.app/Contents
#	mkdir -p validate.app/Contents/MacOS
#	mkdir -p validate.app/Contents/Resources
#	
#	
#	sed -e "s/\$${MACOSX_BUNDLE_GUI_IDENTIFIER}/org.wxwidgets.validate/" \
#	-e "s/\$${MACOSX_BUNDLE_EXECUTABLE_NAME}/validate/" \
#	-e "s/\$${MACOSX_BUNDLE_BUNDLE_NAME}/validate/" \
#	-e "s/\$${MACOSX_BUNDLE_COPYRIGHT}/Copyright 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_BUNDLE_VERSION}/$(WX_VERSION)/" \
#	-e "s/\$${MACOSX_BUNDLE_INFO_STRING}/validate version $(WX_VERSION), (c) 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_LONG_VERSION_STRING}/$(WX_VERSION), (c) 2002-2024 wxWidgets/" \
#	-e "s/\$${MACOSX_BUNDLE_SHORT_VERSION_STRING}/$(WX_RELEASE)/" \
#	$(top_srcdir)/src/osx/carbon/Info.plist.in >validate.app/Contents/Info.plist
#	
#	
#	/bin/echo "APPL????" >validate.app/Contents/PkgInfo
#	
#	
#	ln -f validate$(EXEEXT) validate.app/Contents/MacOS/validate
#	
#	
#	cp -f $(top_srcdir)/src/osx/carbon/wxmac.icns validate.app/Contents/Resources/wxmac.icns

#validate_bundle: $(____validate_BUNDLE_TGT_REF_DEP)

validate_sample_rc.o: $(srcdir)/../../samples/sample.rc
	$(WINDRES) -i$< -o$@    --define __WX$(TOOLKIT)__ $(__WXUNIV_DEFINE_p_1) $(__DEBUG_DEFINE_p_1)  $(__EXCEPTIONS_DEFINE_p_1) $(__RTTI_DEFINE_p_1) $(__THREAD_DEFINE_p_1) --include-dir $(srcdir) $(__DLLFLAG_p_1) $(__WIN32_DPI_MANIFEST_p) --include-dir $(srcdir)/../../samples $(__RCDEFDIR_p) --include-dir $(top_srcdir)/include

validate_validate.o: $(srcdir)/validate.cpp
	$(CXXC) -c -o $@ $(VALIDATE_CXXFLAGS) $(srcdir)/validate.cpp


# Include dependency info, if present:
-include ./.deps/*.d

.PHONY: all install uninstall clean distclean validate_bundle
