Name:		pairs
Summary:	A memory and pairs game for KDE
Version:	4.11.4
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://edu.kde.org/applications/all/pairs
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Suggests:	%{name}-editor

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

%package editor
Summary:	Editor for pairs
Requires:	%{name} = %{EVRD}

%description editor
This package provides an editor for KDE game pairs.

%files editor
%doc %{_kde_docdir}/HTML/en/pairseditor
%{_kde_bindir}/pairseditor
%{_kde_applicationsdir}/pairseditor.desktop
%{_kde_appsdir}/pairseditor/pairseditorui.rc

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.11.0-1
- New version 4.11.0
- Update files list

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- New subpackage editor
- Minor spec cleanup

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4
- Spec cleanup

* Sun Jul 15 2012 Crispin Boylan <crisb@mandriva.org> 4.8.97-1
+ Revision: 809468
- Initial package (from mageia)
- Created package structure for 'pairs'.

