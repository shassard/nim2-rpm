%undefine _debugsource_packages

Summary: A statically typed compiled systems programming language
Name: nim
Version: 1.6.4
Release: 1
License: MIT
Group: Development/Languages
Source: https://nim-lang.org/download/%{name}-%{version}.tar.xz
URL: https://nim-lang.org/
BuildRequires: gcc
BuildRequires: pcre2-devel
BuildRequires: openssl-devel
Requires: compat-openssl11

%description
Nim is a statically typed compiled systems programming language.
It combines successful concepts from mature languages like Python,
Ada and Modula.

%prep
%setup -q

%build
sh build.sh
bin/nim c koch
./koch boot -d:release
./koch tools

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 bin/atlas %{buildroot}/%{_bindir}/atlas
install -m 0755 bin/nim %{buildroot}/%{_bindir}/nim
install -m 0755 bin/nimble %{buildroot}/%{_bindir}/nimble
install -m 0755 bin/nim_dbg %{buildroot}/%{_bindir}/nim_dbg
install -m 0755 bin/nim-gdb %{buildroot}/%{_bindir}/nim-gdb
install -m 0755 bin/nimgrep %{buildroot}/%{_bindir}/nimgrep
install -m 0755 bin/nimpretty %{buildroot}/%{_bindir}/nimpretty
install -m 0755 bin/nimsuggest %{buildroot}/%{_bindir}/nimsuggest
install -m 0755 bin/testament %{buildroot}/%{_bindir}/testament
 
%files
%{_bindir}/*

%changelog
* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.6.4-1
- First build of 1.6.4