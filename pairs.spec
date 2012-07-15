Name: pairs
Summary: A memory and pairs game for KDE
Version: 4.8.97
Release: 1
Group: Education
License: GPLv2 and LGPLv2 and GFDL
URL: http://edu.kde.org/applications/all/pairs
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: desktop-file-utils

%description
Pairs is a game that will help train your memory by remembering different
images, shapes, sounds and text.

%files
%{_kde_bindir}/pairs
%{_kde_applicationsdir}/pairs.desktop
%{_kde_appsdir}/pairs
%{_kde_configdir}/pairs.knsrc
%{_kde_iconsdir}/*/*/*/*

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4  -DKDE4_ENABLE_FINAL=ON
%make

%install
%makeinstall_std -C build

desktop-file-install --dir %{buildroot}%{_kde_applicationsdir} \
	%{buildroot}%{_kde_applicationsdir}/*.desktop

