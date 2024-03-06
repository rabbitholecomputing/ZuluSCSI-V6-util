Name:		zuluscsi-v6-util
Version:	6.4.0
Release:	1%{?dist}
Summary:	ZuluSCSI-V6 utility

License:	GPLv3
URL:		http://www.codesrc.com/mediawiki/index.php?title=SCSI2SD
Source0:	ZuluSCSI-V6-util-6.4.0.tar.bz2

BuildRequires:	wxGTK3-devel
BuildRequires:	zlib-devel
BuildRequires:	hidapi-devel
BuildRequires:	systemd-devel
BuildRequires:	expat-devel
BuildRequires:	gcc-c++
BuildRequires:	make
Requires:	wxGTK3
Requires:	zlib
Requires:	hidapi

%description
ZuluSCSI, a SCSI Hard Drive Emulator for retro computing.

ZuluSCSI is a modern replacement for failed drives. It allows the use of
vintage computer hardware long after their mechanical drives fail. The use of
SD memory cards solves the problem of transferring data between the vintage
computer and a modern PC (who still has access to a working floppy drive ?)

This package provides the tools to manage the ZuluSCSI V6 card:
- scsi2sd-util, to configure it
- scsi2sd-test, to test it

%prep
%setup -q

%build
make USE_SYSTEM=Yes %{?_smp_mflags}

%install
%make_install USE_SYSTEM=Yes

%files
%{_bindir}/zuluSCSI-V6-util
%{_bindir}/zuluSCSI-V6-test

%changelog

