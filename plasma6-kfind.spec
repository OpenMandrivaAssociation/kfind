%define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE utility to find files
Name:		plasma6-kfind
Version:	24.01.96
Release:	%{?git:0.%{git}.}1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/filelight/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kfind/-/archive/%{gitbranch}/kfind-%{gitbranchd}.tar.bz2#/kfind-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kfind-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core5Compat)

%description
The Find Files tool is a useful method of searching for specific files
on your computer, or for searching for files that match a pattern. An
example of this could include searching for files of a particular type or
with certain letters in the filename, or that contain a certain piece of
text in their contents.

KFind is a graphical tool, and not normally run from the command line.

%files -f kfind.lang
%{_datadir}/applications/org.kde.kfind.desktop
%{_bindir}/kfind
%{_docdir}/HTML/*/kfind
%{_iconsdir}/hicolor/*/apps/kfind.*
%{_mandir}/man1/kfind.1*
%{_mandir}/*/man1/kfind.1*
%{_datadir}/metainfo/org.kde.kfind.appdata.xml
%{_datadir}/qlogging-categories6/kfind.categories

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kfind-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kfind
