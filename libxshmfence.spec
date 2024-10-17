# libxshmfence is used by mesa, mesa is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 1
%define libname %mklibname xshmfence %{major}
%define devname %mklibname xshmfence -d
%define lib32name libxshmfence%{major}
%define dev32name libxshmfence-devel

%global optflags %{optflags} -O3

Summary:	Shared memory fence support library for X11, needed for DRI3
Name:		libxshmfence
Version:	1.3.2
Release:	2
URL:		https://xorg.freedesktop.org/
License:	MIT
Group:		System/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)

%description
Shared memory fence support library for X11, needed for DRI3.

%package -n %{libname}
Summary:	Shared memory fence support library for X11, needed for DRI3
Group:		System/Libraries

%description -n %{libname}
Shared memory fence support library for X11, needed for DRI3.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Shared memory fence support library for X11, needed for DRI3 (32-bit)
Group:		System/Libraries
BuildRequires:	libc6

%description -n %{lib32name}
Shared memory fence support library for X11, needed for DRI3.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
Development files (Headers etc.) for %{name}.
%endif

%prep
%autosetup -p1
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/*.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/*
%endif
