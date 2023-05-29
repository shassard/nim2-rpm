%undefine _debugsource_packages

Summary: A statically typed compiled systems programming language
Name: nim
Version: 2.0
Release: 1
License: MIT
Group: Development/Languages
Source: https://github.com/nim-lang/nightlies/releases/download/latest-version-2-0/source.tar.xz
URL: https://nim-lang.org/
BuildRequires: gcc
BuildRequires: pcre2-devel
BuildRequires: openssl-devel
Requires: gcc

%description
Nim is a statically typed compiled systems programming language.
It combines successful concepts from mature languages like Python,
Ada and Modula.

%prep
%setup -q

%build
sh ./build.sh
./bin/nim c koch
./koch boot -d:release
./koch tools

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 bin/* %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
sed -i '1i lib = "%{_datadir}/%{name}/lib"' config/nim.cfg
sed -i '1i path = "%{_datadir}/%{name}"' config/nim.cfg
cp -R config %{buildroot}/%{_datadir}/%{name}/config
cp -R compiler %{buildroot}/%{_datadir}/%{name}/compiler
cp -R doc %{buildroot}/%{_datadir}/%{name}/doc
cp -R lib %{buildroot}/%{_datadir}/%{name}/lib
cp -R nimpretty %{buildroot}/%{_datadir}/%{name}/nimpretty
cp -R nimsuggest %{buildroot}/%{_datadir}/%{name}/nimsuggest
cp -R testament %{buildroot}/%{_datadir}/%{name}/testament
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
ln -f -s -t %{buildroot}/%{_sysconfdir}/%{name} nim.cfg %{_datadir}/%{name}/config/nim.cfg

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
%{_datadir}/%{name}
%{_sysconfdir}/%{name}

%changelog
* Mon May 29 2023 Stephen Hassard <steve@hassard.net> - 2.0-beta-1
- Use upstream latest-version-2.0 sources.
* Mon May 29 2023 Stephen Hassard <steve@hassard.net> - 1.6.12-1
- Bump to upstream 1.6.12
* Wed Nov 23 2022 Stephen Hassard <steve@hassard.net> - 1.6.10-1
- Bump to upstream 1.6.10
- Remove openssl 1.0 compat libs, as 3.0 is supported upstream.
* Tue Sep 27 2022 Stephen Hassard <steve@hassard.net> - 1.6.8-1
- Bump to upstream 1.6.8
* Sat Sep 10 2022 Stephen Hassard <steve@hassard.net> - 1.6.6-5
- Add proper openssl 1.1 libraries based on OS to fix Fedora 36+ usage.
* Sun Aug 28 2022 Stephen Hassard <steve@hassard.net> - 1.6.6-4
- Move config folder, but symlink it to the previous location to improve nimlsp usage.
* Sun Aug 28 2022 Stephen Hassard <steve@hassard.net> - 1.6.6-3
- Rework pathing so we don't litter stuff around the wrong place.
- Add path to nim.cfg so we find bits in the new path layout.
- Add missing doc folder
* Thu Jul 28 2022 Stephen Hassard <steve@hassard.net> - 1.6.6-2
- Add gcc dep for builds
* Thu May 5 2022 Stephen Hassard <steve@hassard.net> - 1.6.6-1
- Update to 1.6.6
* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.6.4-3
- Add library bits for nimlangserver
* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.6.4-2
- Fix missing lib directory
* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.6.4-1
- First build of 1.6.4
