Summary:	A memory and pairs game for KDE
Name:		pairs
Version:	15.04.3
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/applications/all/pairs
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
Suggests:	%{name}-editor

%description
Pairs is a game that will help train your memory by remembering different
images, shapes, sounds and text.

%files
%{_datadir}/applications/kde4/pairs.desktop
%{_datadir}/apps/pairs
%{_bindir}/pairs
%{_datadir}/config/pairs.knsrc
%{_datadir}/appdata/pairs.appdata.xml
%{_iconsdir}/*/*/*/*

#----------------------------------------------------------------------------

%package editor
Summary:	Editor for pairs
Requires:	%{name} = %{EVRD}

%description editor
This package provides an editor for KDE game pairs.

%files editor
%doc %{_docdir}/HTML/en/pairseditor
%{_bindir}/pairseditor
%{_datadir}/applications/kde4/pairseditor.desktop
%{_datadir}/apps/pairseditor/pairseditorui.rc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

