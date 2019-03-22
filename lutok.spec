Summary:	Lightweight C++ API library for Lua
Name:		lutok
Version:	0.4
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	https://github.com/jmmv/lutok/releases/download/%{name}-%{version}/lutok-%{version}.tar.gz
# Source0-md5:	5da43895d9209f8c19d79433dd046b3f
URL:		https://github.com/jmmv/lutok
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libatf-c++-devel >= 0.20
BuildRequires:	libtool
BuildRequires:	lua53-devel

%define _testsdir %{_libexecdir}/lutok/tests

%description
Lutok provides thin C++ wrappers around the Lua C API to ease the
interaction between C++ and Lua. These wrappers make intensive use of
RAII to prevent resource leakage, expose C++-friendly data types,
report errors by means of exceptions and ensure that the Lua stack is
always left untouched in the face of errors. The library also provides
a small subset of miscellaneous utility functions built on top of the
wrappers.

Lutok focuses on providing a clean and safe C++ interface; the
drawback is that it is not suitable for performance-critical
environments. In order to implement error-safe C++ wrappers on top of
a Lua C binary library, Lutok adds several layers or abstraction and
error checking that go against the original spirit of the Lua C API
and thus degrade performance.

%package -n liblutok
Summary:	Lutok library
Group:		Libraries

%description -n liblutok
Lutok provides thin C++ wrappers around the Lua C API to ease the
interaction between C++ and Lua. These wrappers make intensive use of
RAII to prevent resource leakage, expose C++-friendly data types,
report errors by means of exceptions and ensure that the Lua stack is
always left untouched in the face of errors. The library also provides
a small subset of miscellaneous utility functions built on top of the
wrappers.

Lutok focuses on providing a clean and safe C++ interface; the
drawback is that it is not suitable for performance-critical
environments. In order to implement error-safe C++ wrappers on top of
a Lua C binary library, Lutok adds several layers or abstraction and
error checking that go against the original spirit of the Lua C API
and thus degrade performance.

%package -n liblutok-devel
Summary:	Libraries and header files for Lutok development
Requires:	liblutok = %{version}-%{release}
Requires:	lua-devel >= 5.1

%description -n liblutok-devel
Provides the libraries and header files to develop applications that
use the Lutok C++ API to Lua.

%package -n liblutok-static
Summary:	Static liblutok library
Group:		Development/Libraries
Requires:	liblutok-devel = %{version}-%{release}

%description -n liblutok-static
Static liblutok library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-atf=yes \
	--with-doxygen \
	--docdir=%{_docdir}/lutok-doc-%{version} \
	--htmldir=%{_docdir}/lutok-doc-%{version}/html

%{__make} \
	testsdir=%{_testsdir}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA= \
	testsdir=%{_testsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%{_docdir}/lutok-doc-%{version}
%dir %{_libexecdir}/%{name}
%{_testsdir}

%files -n liblutok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblutok.so.3
%attr(755,root,root) %ghost %{_libdir}/liblutok.so.3.0.0

%files -n liblutok-devel
%defattr(644,root,root,755)
%{_includedir}/lutok
%attr(755,root,root) %{_libdir}/liblutok.so
%{_libdir}/liblutok.la
%{_pkgconfigdir}/lutok.pc

%files -n liblutok-static
%defattr(644,root,root,755)
%{_libdir}/liblutok.a

%changelog
