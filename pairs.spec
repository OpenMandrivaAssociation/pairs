Name:		pairs
Summary:	A memory and pairs game for KDE
Version:	4.9.4
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://edu.kde.org/applications/all/pairs
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	desktop-file-utils

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

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

desktop-file-install --dir %{buildroot}%{_kde_applicationsdir} \
	%{buildroot}%{_kde_applicationsdir}/*.desktop


%changelog
* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4
- Spec cleanup

* Sun Jul 15 2012 Crispin Boylan <crisb@mandriva.org> 4.8.97-1
+ Revision: 809468
- Initial package (from mageia)
- Created package structure for 'pairs'.

