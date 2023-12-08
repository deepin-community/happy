%define name    happy
%define version 1.17
%define release 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        BSD-like
Group:          Development/Languages/Haskell
URL:            http://haskell.org/happy/
Source:         http://haskell.org/happy/dist/%{version}/happy-%{version}.tar.gz
Packager:       Sven Panne <sven.panne@aedion.de>
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Prefix:         %{_prefix}
BuildRequires:  ghc, docbook-dtd, docbook-xsl-stylesheets, libxslt, libxml2, fop, xmltex, dvips
Summary:        The LALR(1) Parser Generator for Haskell

%description
Happy is a parser generator system for Haskell, similar to the tool
`yacc' for C. Like `yacc', it takes a file containing an annotated BNF
specification of a grammar and produces a Haskell module containing a
parser for the grammar.

Happy is flexible: you can have several Happy parsers in the same
program, and several entry points to a single grammar. Happy can work
in conjunction with a lexical analyser supplied by the user (either
hand-written or generated by another program), or it can parse a
stream of characters directly (but this isn't practical in most
cases).

Authors:
--------
    Simon Marlow <simonmar@microsoft.com>
    Andy Gill <andy@galconn.com>

%prep
%setup

%build
runhaskell Setup.lhs configure --prefix=%{_prefix} --docdir=%{_datadir}/doc/packages/%{name}
runhaskell Setup.lhs build
cd doc
test -f configure || autoreconf
./configure
make html

%install
runhaskell Setup.lhs copy --destdir=${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc ANNOUNCE
%doc CHANGES
%doc LICENSE
%doc README
%doc TODO
%doc doc/happy
%doc examples
%{prefix}/bin/happy
%{prefix}/share/happy-%{version}
