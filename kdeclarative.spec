%define major 5
%define libname %mklibname KF5Declarative %{major}
%define devname %mklibname KF5Declarative -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdeclarative
Version: 5.67.0
Release: 3
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 framework for integrating with QML
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5Package)
# For QCH format docs
BuildRequires: doxygen >= 1.8.16-2
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 framework for integrating with QML.

%package -n %{libname}
Summary: The KDE Frameworks 5 framework for integrating with QML
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 framework for integrating with QML.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}%{major}

%files -f %{name}%{major}.lang
%{_bindir}/kpackagelauncherqml
%{_libdir}/qt5/qml/org

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs
%{_libdir}/cmake/KF5Declarative

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
