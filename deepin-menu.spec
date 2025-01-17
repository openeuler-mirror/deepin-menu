Name:           deepin-menu
Version:        5.0.1
Release:        4
Summary:        Deepin menu service
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-menu
Source0:        %{name}_%{version}.orig.tar.xz	

BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  dde-qt-dbus-factory-devel
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qt5-qtbase-private-devel

%description
Deepin menu service for building beautiful menus.

%prep
%setup -q
sed -i 's|/usr/bin|%{_libexecdir}|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

%build
%qmake_qt5 DEFINES+=QT_NO_DEBUG_OUTPUT
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%files
%doc README.md
%license LICENSE
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/com.deepin.menu.service

%changelog
* Mon Feb 07 2022 liweigang <liweiganga@uniontech.com> - 5.0.1-4
- fix build error

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.0.1-3
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.1-2
- Package init
