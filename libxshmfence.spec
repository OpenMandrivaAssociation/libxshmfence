%define major 1
%define libname %mklibname xshmfence %{major}
%define devname %mklibname xshmfence -d

Name: libxshmfence
Version: 1.1
Release: 4
Source0: ftp://xorg.freedesktop.org/pub/individual/lib/%{name}-%{version}.tar.bz2
Summary: Shared memory fence support library for X11, needed for DRI3
URL: http://libxshmfence.sf.net/
License: GPL
Group: System/Libraries
BuildRequires: x11-proto-devel

%description
Shared memory fence support library for X11, needed for DRI3

%package -n %{libname}
Summary: Shared memory fence support library for X11, needed for DRI3
Group: System/Libraries

%description -n %{libname}

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%configure2_5x

%build
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
