%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE utility to find files
Name:		kfind
Version:	20.03.90
Release:	1
Epoch:		1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/filelight/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5FileMetaData)

%description
The Find Files tool is a useful method of searching for specific files
on your computer, or for searching for files that match a pattern. An
example of this could include searching for files of a particular type or
with certain letters in the filename, or that contain a certain piece of
text in their contents.

KFind is a graphical tool, and not normally run from the command line.

%files -f %{name}.lang
%{_kde5_applicationsdir}/org.kde.kfind.desktop
%{_bindir}/kfind
%{_docdir}/HTML/*/kfind
%{_iconsdir}/hicolor/*/apps/kfind.*
%{_mandir}/man1/kfind.1*
%{_mandir}/*/man1/kfind.1*
%{_datadir}/metainfo/org.kde.kfind.appdata.xml
%{_datadir}/qlogging-categories5/kfind.categories

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
