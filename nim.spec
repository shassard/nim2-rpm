%undefine _debugsource_packages

Summary: A statically typed compiled systems programming language
Name: nim
Version: 1.6.6
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
install -m 0755 bin/* %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
cp -R lib %{buildroot}/%{_libdir}/nim
cp -R compiler %{buildroot}/%{_prefix}/compiler
cp -R nimpretty %{buildroot}/%{_prefix}/nimpretty
cp -R nimsuggest %{buildroot}/%{_prefix}/nimsuggest
cp -R testament %{buildroot}/%{_prefix}/testament
sed -i '1i lib = "/usr/lib64/nim"' config/nim.cfg
mkdir -p %{buildroot}/%{_sysconfdir}/nim
install config/nim.cfg %{buildroot}/%{_sysconfdir}/nim

%files
%{_bindir}/atlas
%{_bindir}/nim
%{_bindir}/nimble
%{_bindir}/nim_dbg
%{_bindir}/nim-gdb
%{_bindir}/nimgrep
%{_bindir}/nimpretty
%{_bindir}/nimsuggest
%{_bindir}/testament
%{_libdir}/nim
%{_prefix}/compiler
%{_prefix}/nimpretty
%{_prefix}/nimsuggest
%{_prefix}/testament
%{_sysconfdir}/nim/nim.cfg

%changelog
* Thu May 5 2022 Stephen Hassard <steve@hassard.net> - 1.6.6-1
- Update to 1.6.6
* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.6.4-3
- Add library bits for nimlangserver
* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.6.4-2
- Fix missing lib directory
* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.6.4-1
- First build of 1.6.4
