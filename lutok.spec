Summary:	Lightweight C++ API library for Lua
Summary(pl.UTF-8):	Lekka biblioteka API C++ dla Lua
Name:		lutok
Version:	0.4
Release:	4
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/jmmv/lutok/releases
Source0:	https://github.com/jmmv/lutok/releases/download/%{name}-%{version}/lutok-%{version}.tar.gz
# Source0-md5:	5da43895d9209f8c19d79433dd046b3f
Patch0:		%{name}-default-lua.patch
URL:		https://github.com/jmmv/lutok
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.9
BuildRequires:	libatf-c++-devel >= 0.20
BuildRequires:	libatf-sh-devel >= 0.20
BuildRequires:	libtool >= 2:2
BuildRequires:	lua-devel >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pkgtestsdir	%{_libexecdir}/lutok/tests

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

%description -l pl.UTF-8
Lutok udostępnia cienką warstwę obudowującą API C języka Lua, aby
ułatwić współpracę między C++ a Lua. Interfejsy te intensywnie
wykorzystują RAII (aby zapobiec wyciekowi zasobów), udostępniają
typy danych przyjazne dla C++, zgłaszają błędy poprzez wyjątki i
zapewniają, że stos Lua jest nienaruszony w przypadku błędów.
Biblioteka udostępnia także mały podzbiór różnych funkcji
narzędziowych, zbudowanych w oparciu o te interfejsy.

Lutok skupia się na zapewnieniu czystego i bezpiecznego interfejsu
C++; wadą jest to, że nie nadaje się w środowisku, gdzie krytyczna
jest wydajność. Aby zaimplementować bezpieczne pod kątem błędów
interfejsy C++ w oparciu o bibliotekę binarną C Lua, Lutok dodaje
kilka warstw lub abstrakcji oraz sprawdzania błędów, niezgodnych z
duchem API C Lua i zmniejszających wydajność.

%package -n liblutok
Summary:	Lutok library
Summary(pl.UTF-8):	Biblioteka Lutok
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

%description -n liblutok -l pl.UTF-8
Lutok udostępnia cienką warstwę obudowującą API C języka Lua, aby
ułatwić współpracę między C++ a Lua. Interfejsy te intensywnie
wykorzystują RAII (aby zapobiec wyciekowi zasobów), udostępniają
typy danych przyjazne dla C++, zgłaszają błędy poprzez wyjątki i
zapewniają, że stos Lua jest nienaruszony w przypadku błędów.
Biblioteka udostępnia także mały podzbiór różnych funkcji
narzędziowych, zbudowanych w oparciu o te interfejsy.

Lutok skupia się na zapewnieniu czystego i bezpiecznego interfejsu
C++; wadą jest to, że nie nadaje się w środowisku, gdzie krytyczna
jest wydajność. Aby zaimplementować bezpieczne pod kątem błędów
interfejsy C++ w oparciu o bibliotekę binarną C Lua, Lutok dodaje
kilka warstw lub abstrakcji oraz sprawdzania błędów, niezgodnych z
duchem API C Lua i zmniejszających wydajność.

%package -n liblutok-devel
Summary:	Header files for Lutok development
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Lutok
Requires:	liblutok = %{version}-%{release}
Requires:	lua-devel >= 5.1

%description -n liblutok-devel
The header files to develop applications that use the Lutok C++ API to
Lua.

%description -n liblutok-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji wykorzystująch API C++
biblioteki Lutok do Lua.

%package -n liblutok-static
Summary:	Static liblutok library
Summary(pl.UTF-8):	Statyczna biblioteka liblutok
Group:		Development/Libraries
Requires:	liblutok-devel = %{version}-%{release}

%description -n liblutok-static
Static liblutok library.

%description -n liblutok-static -l pl.UTF-8
Statyczna biblioteka liblutok.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--docdir=%{_docdir}/lutok-doc-%{version} \
	--htmldir=%{_docdir}/lutok-doc-%{version}/html \
	--with-atf \
	--with-doxygen

%{__make} \
	testsdir=%{pkgtestsdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA= \
	testsdir=%{pkgtestsdir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblutok.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n liblutok -p /sbin/ldconfig
%postun	-n liblutok -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%doc %{_docdir}/lutok-doc-%{version}
%dir %{_libexecdir}/%{name}
%{pkgtestsdir}

%files -n liblutok
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblutok.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblutok.so.3

%files -n liblutok-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblutok.so
%{_includedir}/lutok
%{_pkgconfigdir}/lutok.pc

%files -n liblutok-static
%defattr(644,root,root,755)
%{_libdir}/liblutok.a
