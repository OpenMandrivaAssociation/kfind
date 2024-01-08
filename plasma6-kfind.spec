%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE utility to find files
Name:		plasma6-kfind
Version:	24.01.85
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/filelight/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kfind-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KDELibs4Support)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6FileMetaData)

%description
The Find Files tool is a useful method of searching for specific files
on your computer, or for searching for files that match a pattern. An
example of this could include searching for files of a particular type or
with certain letters in the filename, or that contain a certain piece of
text in their contents.

KFind is a graphical tool, and not normally run from the command line.

%files -f %{name}.lang
%{_kde6_applicationsdir}/org.kde.kfind.desktop
%{_bindir}/kfind
%{_docdir}/HTML/*/kfind
%{_iconsdir}/hicolor/*/apps/kfind.*
%{_mandir}/man1/kfind.1*
%{_mandir}/*/man1/kfind.1*
%{_datadir}/metainfo/org.kde.kfind.appdata.xml
%{_datadir}/qlogging-categories6/kfind.categories

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
