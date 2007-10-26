## @file
# This file is used to define each component of INF file
#
# Copyright (c) 2007, Intel Corporation
# All rights reserved. This program and the accompanying materials
# are licensed and made available under the terms and conditions of the BSD License
# which accompanies this distribution.  The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#

##
# Import Modules
#
import os
import EdkLogger
from CommonDataClass.CommonClass import LibraryClassClass
from CommonDataClass.ModuleClass import *
from String import *
from DataType import *
from Identification import *
from Dictionary import *
from BuildToolError import *

## InfObject
#
# This class defined basic Inf object which is used by inheriting
# 
# @param object:       Inherited from object class
#
class InfObject(object):
    def __init__(self):
        object.__init__()

## InfDefines
#
# This class defined basic Defines used in Inf object
# 
# @param InfObject:        Inherited from InfObject class
#
# @var DefinesDictionary:  To store value for DefinesDictionary 
#
class InfDefines(InfObject):
    def __init__(self):
        self.DefinesDictionary = {
            #
            # Required Fields
            #
            TAB_INF_DEFINES_BASE_NAME                               : [''],
            TAB_INF_DEFINES_FILE_GUID                               : [''],
            TAB_INF_DEFINES_MODULE_TYPE                             : [''],
            TAB_INF_DEFINES_EFI_SPECIFICATION_VERSION               : [''],
            TAB_INF_DEFINES_EDK_RELEASE_VERSION                     : [''],
            
            #
            # Optional Fields
            #
            TAB_INF_DEFINES_INF_VERSION                             : [''],
            TAB_INF_DEFINES_BINARY_MODULE                           : [''],
            TAB_INF_DEFINES_LIBRARY_CLASS                           : [''],
            TAB_INF_DEFINES_COMPONENT_TYPE                          : [''],
            TAB_INF_DEFINES_MAKEFILE_NAME                           : [''],
            TAB_INF_DEFINES_BUILD_NUMBER                            : [''],
            TAB_INF_DEFINES_BUILD_TYPE                              : [''],
            TAB_INF_DEFINES_FFS_EXT                                 : [''],
            TAB_INF_DEFINES_FV_EXT                                  : [''],
            TAB_INF_DEFINES_SOURCE_FV                               : [''],
            TAB_INF_DEFINES_VERSION_NUMBER                          : [''],
            TAB_INF_DEFINES_VERSION_STRING                          : [''],
            TAB_INF_DEFINES_PCD_IS_DRIVER                           : [''],
            TAB_INF_DEFINES_TIANO_R8_FLASHMAP_H                     : [''],
            TAB_INF_DEFINES_ENTRY_POINT                             : [''],
            TAB_INF_DEFINES_UNLOAD_IMAGE                            : [''],
            TAB_INF_DEFINES_CONSTRUCTOR                             : [''],
            TAB_INF_DEFINES_DESTRUCTOR                              : [''],
            TAB_INF_DEFINES_DEFINE                                  : [''],
            TAB_INF_DEFINES_SPEC                                    : [''],
            TAB_INF_DEFINES_CUSTOM_MAKEFILE                         : [''],
            TAB_INF_DEFINES_SHADOW                                  : ['']
        }

## InfContents
#
# This class defined basic Contents used in Inf object
# 
# @param InfObject:   Inherited from InfObject class
#
# @var Sources:       To store value for Sources
# @var BuildOptions:  To store value for BuildOptions
# @var Binaries:      To store value for Binaries
# @var Includes:      To store value for Includes
# @var Guids:         To store value for Guids
# @var Protocols:     To store value for Protocols
# @var Ppis:          To store value for Ppis
# @var Libraries:     To store value for Libraries
# @var Packages:      To store value for Packages
# @var FixedPcd:      To store value for FixedPcd
# @var PatchPcd:      To store value for PatchPcd
# @var Pcd:           To store value for Pcd
# @var PcdEx:         To store value for PcdEx
# @var Depex:         To store value for Depex
# @var Nmake:         To store value for Nmake
#
class InfContents(InfObject):
    def __init__(self):
        self.Sources = []
        self.BuildOptions = []
        self.Binaries = []
        self.Includes = []
        self.Guids = []
        self.Protocols = []
        self.Ppis = []
        self.Libraries = []
        self.LibraryClasses = []
        self.Packages = []
        self.FixedPcd = []
        self.PatchPcd = []
        self.FeaturePcd = []
        self.Pcd = []
        self.PcdEx = []
        self.Depex = []
        self.Nmake = []

## Inf
#
# This class defined the structure used in Inf object
# 
# @param InfObject:         Inherited from InfObject class
# @param Ffilename:         Input value for Ffilename of Inf file, default is None
# @param IsMergeAllArches:  Input value for IsMergeAllArches
#                           True is to merge all arches
#                           Fales is not to merge all arches
#                           default is False
# @param IsToModule:        Input value for IsToModule
#                           True is to transfer to ModuleObject automatically
#                           False is not to transfer to ModuleObject automatically
#                           default is False
# @param WorkspaceDir:      Input value for current workspace directory, default is None
#
# @var Identification:      To store value for Identification, it is a structure as Identification
# @var Defines:             To store value for Defines, it is a structure as InfDefines
# @var UserExtensions:      To store value for UserExtensions
# @var Module:              To store value for Module, it is a structure as ModuleClass
# @var WorkspaceDir:        To store value for WorkspaceDir
# @var Contents:            To store value for Contents, it is a structure as InfContents
# @var KeyList:             To store value for KeyList, a list for all Keys used in Dec
#
class Inf(InfObject):
    def __init__(self, Filename = None, IsMergeAllArches = False, IsToModule = False, WorkspaceDir = None):
        self.Identification = Identification()
        self.Defines = InfDefines()
        self.Contents = {}
        self.UserExtensions = ''
        self.Module = ModuleClass()
        self.WorkspaceDir = WorkspaceDir
        
        for Arch in DataType.ARCH_LIST_FULL:
            self.Contents[Arch] = InfContents()

        self.KeyList = [
            TAB_SOURCES, TAB_BUILD_OPTIONS, TAB_BINARIES, TAB_INCLUDES, TAB_GUIDS, TAB_PROTOCOLS, TAB_PPIS, TAB_LIBRARY_CLASSES, TAB_PACKAGES, TAB_LIBRARIES, \
            TAB_INF_FIXED_PCD, TAB_INF_PATCH_PCD, TAB_INF_FEATURE_PCD, TAB_INF_PCD, TAB_INF_PCD_EX, TAB_DEPEX, TAB_NMAKE
        ]

        #
        # Load Inf file if filename is not None
        #
        if Filename != None:
            self.LoadInfFile(Filename)
        
        #
        # Merge contents of Inf from all arches if IsMergeAllArches is True
        #        
        if IsMergeAllArches:
            self.MergeAllArches()

        #
        # Transfer to Module Object if IsToModule is True
        #
        if IsToModule:
            self.InfToModule()

    ## Merge contents of Inf from all arches
    #
    # Find the contents defined in all arches and merge them to all
    #
    def MergeAllArches(self):
        for Key in self.KeyList:
            for Arch in DataType.ARCH_LIST:
                Command = "self.Contents[Arch]." + Key + ".extend(" + "self.Contents['" + DataType.TAB_ARCH_COMMON + "']." + Key + ")"
                eval(Command)     

    ## Parse Inf file
    #
    # Go through input lines one by one to find the value defined in Key section.
    # Save them to KeyField
    #
    # @param Lines:     Lines need to be parsed
    # @param Key:       The key value of the section to be located
    # @param KeyField:  To save the found contents
    #
    def ParseInf(self, Lines, Key, KeyField):
        newKey = SplitModuleType(Key)
        if newKey[0].upper().find(DataType.TAB_LIBRARY_CLASSES.upper()) != -1:
            GetLibraryClassesWithModuleType(Lines, Key, KeyField, TAB_COMMENT_SPLIT)
        else:
            GetMultipleValuesOfKeyFromLines(Lines, Key, KeyField, TAB_COMMENT_SPLIT)

    ## Transfer to Module Object
    # 
    # Transfer all contents of an Inf file to a standard Module Object
    #
    def InfToModule(self):
        #
        # Get value for Header
        #
        self.Module.Header.Name = self.Defines.DefinesDictionary[TAB_INF_DEFINES_BASE_NAME][0]
        self.Module.Header.Guid = self.Defines.DefinesDictionary[TAB_INF_DEFINES_FILE_GUID][0]
        
        #
        # Get version of INF
        #
        VersionNumber = self.Defines.DefinesDictionary[TAB_INF_DEFINES_VERSION_NUMBER][0]
        VersionString = self.Defines.DefinesDictionary[TAB_INF_DEFINES_VERSION_STRING][0]
        if len(VersionNumber) > 0 and len(VersionString) == 0:
            EdkLogger.warn(2000, 'VERSION_NUMBER depricated; INF file %s should be modified to use VERSION_STRING instead.' % self.Identification.FileFullPath)
            self.Module.Header.Version = VersionNumber
        if len(VersionString) > 0:
            if len(VersionNumber) > 0:
                EdkLogger.warn(2001, 'INF file %s defines both VERSION_NUMBER and VERSION_STRING, using VERSION_STRING' % self.Identification.FileFullPath)
            self.Module.Header.Version = VersionString
        
        self.Module.Header.FileName = self.Identification.FileName
        self.Module.Header.FullPath = self.Identification.FileFullPath
        File = self.Module.Header.FullPath
        
        self.Module.Header.EfiSpecificationVersion = self.Defines.DefinesDictionary[TAB_INF_DEFINES_EFI_SPECIFICATION_VERSION][0]
        self.Module.Header.EdkReleaseVersion = self.Defines.DefinesDictionary[TAB_INF_DEFINES_EDK_RELEASE_VERSION][0]
        self.Module.Header.InfVersion = self.Defines.DefinesDictionary[TAB_INF_DEFINES_INF_VERSION][0]
                
        self.Module.Header.ModuleType = self.Defines.DefinesDictionary[TAB_INF_DEFINES_MODULE_TYPE][0]
        self.Module.Header.BinaryModule = self.Defines.DefinesDictionary[TAB_INF_DEFINES_BINARY_MODULE][0]
        self.Module.Header.ComponentType = self.Defines.DefinesDictionary[TAB_INF_DEFINES_COMPONENT_TYPE][0]
        self.Module.Header.MakefileName = self.Defines.DefinesDictionary[TAB_INF_DEFINES_MAKEFILE_NAME][0]
        self.Module.Header.BuildNumber = self.Defines.DefinesDictionary[TAB_INF_DEFINES_BUILD_NUMBER][0]
        self.Module.Header.BuildType = self.Defines.DefinesDictionary[TAB_INF_DEFINES_BUILD_TYPE][0]
        self.Module.Header.FfsExt = self.Defines.DefinesDictionary[TAB_INF_DEFINES_FFS_EXT][0]
        self.Module.Header.FvExt = self.Defines.DefinesDictionary[TAB_INF_DEFINES_FV_EXT][0]
        self.Module.Header.SourceFv = self.Defines.DefinesDictionary[TAB_INF_DEFINES_SOURCE_FV][0]
        self.Module.Header.PcdIsDriver = self.Defines.DefinesDictionary[TAB_INF_DEFINES_PCD_IS_DRIVER][0]
        self.Module.Header.TianoR8FlashMap_h = self.Defines.DefinesDictionary[TAB_INF_DEFINES_TIANO_R8_FLASHMAP_H][0]
        self.Module.Header.Shadow = self.Defines.DefinesDictionary[TAB_INF_DEFINES_SHADOW][0]
        
        #
        # LibraryClass of Defines
        #
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_LIBRARY_CLASS][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_LIBRARY_CLASS]:
                List = GetSplitValueList(Item, DataType.TAB_VALUE_SPLIT, 1)
                Lib = LibraryClassClass()
                Lib.LibraryClass = CleanString(List[0])
                if len(List) == 1:
                    Lib.SupModuleList = DataType.SUP_MODULE_LIST
                elif len(List) == 2:
                    Lib.SupModuleList = GetSplitValueList(CleanString(List[1]), ' ')
                self.Module.Header.LibraryClass.append(Lib)
        
        #
        # Custom makefile of Defines
        #
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_CUSTOM_MAKEFILE][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_CUSTOM_MAKEFILE]:
                List = Item.split(DataType.TAB_VALUE_SPLIT)
                if len(List) == 2:
                    self.Module.Header.CustomMakefile[CleanString(List[0])] = CleanString(List[1])
                else:
                    RaiseParserError(Item, 'CUSTOM_MAKEFILE of Defines', File, 'CUSTOM_MAKEFILE=<Family>|<Filename>')
        
        #
        # EntryPoint and UnloadImage of Defines
        #
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_ENTRY_POINT][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_ENTRY_POINT]:
                Image = ModuleExternImageClass()
                Image.ModuleEntryPoint = CleanString(Item)
                self.Module.ExternImages.append(Image)
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_UNLOAD_IMAGE][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_UNLOAD_IMAGE]:
                Image = ModuleExternImageClass()
                Image.ModuleUnloadImage = CleanString(Item)
                self.Module.ExternImages.append(Image)
        
        #
        # Constructor and Destructor of Defines
        #
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_CONSTRUCTOR][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_CONSTRUCTOR]:
                LibraryClass = ModuleExternLibraryClass()
                LibraryClass.Constructor = CleanString(Item)
                self.Module.ExternLibraries.append(LibraryClass)
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_DESTRUCTOR][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_DESTRUCTOR]:
                LibraryClass = ModuleExternLibraryClass()
                LibraryClass.Destructor = CleanString(Item)
                self.Module.ExternLibraries.append(LibraryClass)
        
        #
        # Define of Defines
        #
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_DEFINE][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_DEFINE]:
                List = Item.split(DataType.TAB_EQUAL_SPLIT)
                if len(List) != 2:
                    RaiseParserError(Item, 'DEFINE of Defines', File, 'DEFINE <Word> = <Word>')
                else:
                    self.Module.Header.Define[CleanString(List[0])] = CleanString(List[1])
        
        #
        # Spec
        #
        if self.Defines.DefinesDictionary[TAB_INF_DEFINES_SPEC][0] != '':
            for Item in self.Defines.DefinesDictionary[TAB_INF_DEFINES_SPEC]:
                List = Item.split(DataType.TAB_EQUAL_SPLIT)
                if len(List) != 2:
                    RaiseParserError(Item, 'SPEC of Defines', File, 'SPEC <Word> = <Version>')
                else:
                    self.Module.Header.Specification[CleanString(List[0])] = CleanString(List[1])
                
        #
        # BuildOptions
        # [<Family>:]<ToolFlag>=Flag
        #
        BuildOptions = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].BuildOptions:
                MergeArches(BuildOptions, GetBuildOption(Item, File), Arch)
        for Key in BuildOptions.keys():
            BuildOption = BuildOptionClass(Key[0], Key[1], Key[2])
            BuildOption.SupArchList = BuildOptions[Key]
            self.Module.BuildOptions.append(BuildOption)    
        
        #
        # Includes
        #
        Includes = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Includes:
                MergeArches(Includes, Item, Arch)
        for Key in Includes.keys():
            Include = IncludeClass()
            Include.FilePath = Key
            Include.SupArchList = Includes[Key]
            self.Module.Includes.append(Include)
        
        #
        # Libraries
        #
        Libraries = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Libraries:
                MergeArches(Libraries, Item, Arch)
        for Key in Libraries.keys():
            Library = ModuleLibraryClass()
            Library.Library = Key
            Library.SupArchList = Libraries[Key]
            self.Module.Libraries.append(Library)
        
        #
        # LibraryClasses
        # LibraryClass[|<LibraryClassInstanceFilename>[|<TokenSpaceGuidCName>.<PcdCName>]]
        #
        LibraryClasses = {}
        Defines = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].LibraryClasses:
                Status = GenDefines(Item[0], Arch, Defines)
                #
                # Find DEFINE statement
                #
                if Status == 0:
                    pass
                #
                # Find DEFINE statement but in wrong format
                #
                elif Status == -1:
                    RaiseParserError(Item[0], 'LibraryClasses', File, 'DEFINE <VarName> = <PATH>')
                #
                # Not find DEFINE statement
                #
                elif Status == 1:
                    #
                    # { (LibraryClass, Instance, PcdFeatureFlag, ModuleType1|ModuleType2|ModuleType3) : [Arch1, Arch2, ...] }
                    #
                    ItemList = GetSplitValueList((Item[0] + DataType.TAB_VALUE_SPLIT * 2))
                    CheckFileType(ItemList[1], '.Inf', self.Module.Header.FullPath, 'LibraryClasses', Item[0])
                    CheckFileExist(self.WorkspaceDir, ItemList[1], self.Module.Header.FullPath, 'LibraryClasses', Item[0])
                    CheckPcdTokenInfo(ItemList[2], 'LibraryClasses', File)
                    MergeArches(LibraryClasses, (ItemList[0], ItemList[1], ItemList[2], DataType.TAB_VALUE_SPLIT.join(Item[1])), Arch)
        for Key in LibraryClasses.keys():
            KeyList = Key[0].split(DataType.TAB_VALUE_SPLIT)
            LibraryClass = LibraryClassClass()
            LibraryClass.Define = Defines
            LibraryClass.LibraryClass = Key[0]
            LibraryClass.RecommendedInstance = Key[1]
            LibraryClass.FeatureFlag = Key[2]
            LibraryClass.SupArchList = LibraryClasses[Key]
            if Key[3] != '':
                LibraryClass.SupModuleList = GetSplitValueList(Key[3])
            else:
                LibraryClass.SupModuleList = DataType.SUP_MODULE_LIST
            self.Module.LibraryClasses.append(LibraryClass)
        
        #
        # Packages
        #
        Packages = {}
        Defines = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Packages:
                Status = GenDefines(Item, Arch, Defines)
                #
                # Find DEFINE statement
                #
                if Status == 0:
                    pass
                #
                # Find DEFINE statement but in wrong format
                #
                elif Status == -1:
                    RaiseParserError(Item[0], 'Packages', File, 'DEFINE <VarName> = <PATH>')
                #
                # Not find DEFINE statement
                #
                elif Status == 1:
                    CheckFileType(Item, '.Dec', self.Module.Header.FullPath, 'package', Item)
                    CheckFileExist(self.WorkspaceDir, Item, self.Module.Header.FullPath, 'Packages', Item)
                    MergeArches(Packages, Item, Arch)
        for Key in Packages.keys():
            Package = ModulePackageDependencyClass()
            Package.Define = Defines
            Package.FilePath = Key
            Package.SupArchList = Packages[Key]
            self.Module.PackageDependencies.append(Package)
            
        #
        # Nmake
        #
        Nmakes = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Nmake:
                MergeArches(Nmakes, Item, Arch)
        for Key in Nmakes.keys():
            List = GetSplitValueList(Key, DataType.TAB_EQUAL_SPLIT)
            if len(List) != 2:
                RaiseParserError(Item[0], 'Nmake', File, 'DEFINE <VarName> = <PATH>')
            Nmake = ModuleNmakeClass()
            Nmake.Name = List[0]
            Nmake.Value = List[1]
            Nmake.SupArchList = Nmakes[Key]
            self.Module.Nmake.append(Nmake)
        
        #
        # Pcds
        # <TokenSpaceGuidCName>.<PcdCName>[|<Value>]
        #
        Pcds = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].FixedPcd:
                #
                # Library should not have FixedPcd
                #
                if self.Module.Header.LibraryClass != {}:
                    pass
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_FIXED_AT_BUILD, File), Arch)
            
            for Item in self.Contents[Arch].PatchPcd:
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_PATCHABLE_IN_MODULE, File), Arch)
            
            for Item in self.Contents[Arch].FeaturePcd:
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_FEATURE_FLAG, File), Arch)
            
            for Item in self.Contents[Arch].PcdEx:
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_DYNAMIC_EX, File), Arch)
            
            for Item in self.Contents[Arch].Pcd:
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_DYNAMIC, File), Arch)
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_DYNAMIC_EX, File), Arch)
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_FEATURE_FLAG, File), Arch)
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_FIXED_AT_BUILD, File), Arch)
                MergeArches(Pcds, self.GetPcdOfInf(Item, TAB_PCDS_PATCHABLE_IN_MODULE, File), Arch)
                
        for Key in Pcds.keys():
            Pcd = PcdClass()
            Pcd.CName = Key[1]
            Pcd.TokenSpaceGuidCName = Key[0]
            Pcd.DefaultValue = Key[2]
            Pcd.ItemType = Key[3]
            Pcd.SupArchList = Pcds[Key]
            self.Module.PcdCodes.append(Pcd)
        
        #
        # Sources
        # <Filename>[|<Family>[|<TagName>[|<ToolCode>[|<PcdFeatureFlag>]]]]
        #
        Sources = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Sources:
                ItemNew = Item + DataType.TAB_VALUE_SPLIT * 4
                List = GetSplitValueList(ItemNew)
                if len(List) < 5 or len(List) > 9:
                    RaiseParserError(Item, 'Sources', File, '<Filename>[|<Family>[|<TagName>[|<ToolCode>[|<PcdFeatureFlag>]]]]')
                CheckFileExist(self.Identification.FileRelativePath, List[0], File, 'Sources', Item)
                CheckPcdTokenInfo(List[4], 'Sources', File)
                MergeArches(Sources, (List[0], List[1], List[2], List[3], List[4]), Arch)
        for Key in Sources.keys():
            Source = ModuleSourceFileClass(Key[0], Key[2], Key[3], Key[1], Key[4], Sources[Key])
            self.Module.Sources.append(Source)

        #
        # UserExtensions
        #
        if self.UserExtensions != '':
            UserExtension = UserExtensionsClass()
            Lines = self.UserExtensions.splitlines()
            List = GetSplitValueList(Lines[0], DataType.TAB_SPLIT, 2)
            if len(List) != 3:
                RaiseParserError(Lines[0], 'UserExtensions', File, "UserExtensions.UserId.'Identifier'")
            else:
                UserExtension.UserID = List[1]
                UserExtension.Identifier = List[2][0:-1].replace("'", '').replace('\"', '')
                for Line in Lines[1:]:
                    UserExtension.Content = UserExtension.Content + CleanString(Line) + '\n'
            self.Module.UserExtensions.append(UserExtension)
        
        #
        # Guids
        #
        Guids = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Guids:
                MergeArches(Guids, Item, Arch)
        for Key in Guids.keys():
            Guid = GuidClass()
            Guid.CName = Key
            Guid.SupArchList = Guids[Key]
            self.Module.Guids.append(Guid)

        #
        # Protocols
        #
        Protocols = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Protocols:
                MergeArches(Protocols, Item, Arch)
        for Key in Protocols.keys():
            Protocol = ProtocolClass()
            Protocol.CName = Key
            Protocol.SupArchList = Protocols[Key]
            self.Module.Protocols.append(Protocol)
        
        #
        # Ppis
        #
        Ppis = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Ppis:
                MergeArches(Ppis, Item, Arch)
        for Key in Ppis.keys():
            Ppi = PpiClass()
            Ppi.CName = Key
            Ppi.SupArchList = Ppis[Key]
            self.Module.Ppis.append(Ppi)
        
        #
        # Depex
        #
        Depex = {}
        Defines = {}
        for Arch in DataType.ARCH_LIST:
            Line = ''
            for Item in self.Contents[Arch].Depex:
                Status = GenDefines(Item, Arch, Defines)
                #
                # Find DEFINE statement
                #
                if Status == 0:
                    pass
                #
                # Find DEFINE statement but in wrong format
                #
                elif Status == -1:
                    RaiseParserError(Item, 'Depex', File, 'DEFINE <VarName> = <PATH>')
                #
                # Not find DEFINE statement
                #
                elif Status == 1:
                    Line = Line + Item + ' '
            MergeArches(Depex, Line, Arch)
        for Key in Depex.keys():
            Dep = ModuleDepexClass()
            Dep.Depex = Key
            Dep.SupArchList = Depex[Key]
            Dep.Define = Defines
            self.Module.Depex.append(Dep)
        
        #
        # Binaries
        # <FileType>|<Filename>|<Target>[|<TokenSpaceGuidCName>.<PcdCName>]
        #
        Binaries = {}
        for Arch in DataType.ARCH_LIST:
            for Item in self.Contents[Arch].Binaries:
                ItemNew = Item + DataType.TAB_VALUE_SPLIT
                List = GetSplitValueList(ItemNew)
                if len(List) != 4 and len(List) != 5:
                    RaiseParserError(Item, 'Binaries', File, "<FileType>|<Filename>|<Target>[|<TokenSpaceGuidCName>.<PcdCName>]")
                else:
                    CheckPcdTokenInfo(List[3], 'Binaries', File)
                    MergeArches(Binaries, (List[0], List[1], List[2], List[3]), Arch)
        for Key in Binaries.keys():
            Binary = ModuleBinaryFileClass(Key[1], Key[0], Key[2], Key[3], Binaries[Key])
            self.Module.Binaries.append(Binary)
        
    ## Get Pcd Values of Inf
    #
    # Get Pcd of Inf as <TokenSpaceGuidCName>.<PcdCName>[|<Value>]
    #
    # @param Item:  The string describes pcd
    # @param Type:  The type of Pcd
    # @param File:  The file which describes the pcd, used for error report
    #
    # @retval (TokenSpcCName, TokenCName, Value, ItemType) Formatted Pcd Item
    #
    def GetPcdOfInf(self, Item, Type, File):
        Format = '<TokenSpaceGuidCName>.<PcdCName>[|<Value>]'
        InfType = ''
        if Type == TAB_PCDS_FIXED_AT_BUILD:
            InfType = TAB_INF_FIXED_PCD
        elif Type == TAB_PCDS_PATCHABLE_IN_MODULE:
            InfType = TAB_INF_PATCH_PCD
        elif Type == TAB_PCDS_FEATURE_FLAG:
            InfType = TAB_INF_FEATURE_PCD        
        elif Type == TAB_PCDS_DYNAMIC_EX:
            InfType = TAB_INF_PCD_EX        
        elif Type == TAB_PCDS_DYNAMIC:
            InfType = TAB_INF_PCD
        List = GetSplitValueList(Item + DataType.TAB_VALUE_SPLIT)
        if len(List) < 2 or len(List) > 3:
            RaiseParserError(Item, InfType, File, Format)
        TokenInfo = GetSplitValueList(List[0], DataType.TAB_SPLIT)
        if len(TokenInfo) != 2:
            RaiseParserError(Item, InfType, File, Format)
        if len(List) == 3 and List[1] == '':
            #
            # Value is empty
            #
            RaiseParserError(Item, 'Pcds' + Type, File, Format)

        return (TokenInfo[0], TokenInfo[1], List[1], Type)

    ## Load Inf file
    #
    # Load the file if it exists
    #
    # @param Filename:  Input value for filename of Inf file
    #
    def LoadInfFile(self, Filename):     
        (Filepath, Name) = os.path.split(Filename)
        self.Identification.FileName = Name
        self.Identification.FileFullPath = Filename
        self.Identification.FileRelativePath = Filepath
        
        F = open(Filename, 'r').read()
        PreCheck(Filename, F, self.KeyList)
        Sects = F.split(DataType.TAB_SECTION_START)
        for Sect in Sects:
            TabList = GetSplitValueList(Sect.split(TAB_SECTION_END, 1)[0], DataType.TAB_COMMA_SPLIT)
            for Tab in TabList:            
                if Tab.upper() == TAB_INF_DEFINES.upper():
                    GetSingleValueOfKeyFromLines(Sect, self.Defines.DefinesDictionary, TAB_COMMENT_SPLIT, TAB_EQUAL_SPLIT, False, None)
                    continue
                if Tab.upper().find(DataType.TAB_USER_EXTENSIONS.upper()) > -1:
                    self.UserExtensions = Sect
                    continue
                for Arch in DataType.ARCH_LIST_FULL + [DataType.TAB_ARCH_NULL]:
                    for Key in self.KeyList:
                        if Arch != DataType.TAB_ARCH_NULL:
                            Target = (Key + DataType.TAB_SPLIT + Arch).upper()
                        else:
                            Target = Key.upper()
                        if SplitModuleType(Tab)[0].upper() == Target:
                            if Arch != DataType.TAB_ARCH_NULL:
                                Command = 'self.ParseInf(Sect, Tab, self.Contents[Arch].' + Key + ')'
                                eval(Command)
                                continue
                            else:
                                Command = "self.ParseInf(Sect, Tab, self.Contents['" + DataType.TAB_ARCH_COMMON + "']." + Key + ')'
                                eval(Command)
                                continue
            #EndFor

    ## Show detailed information of Inf
    #
    # Print all members and their values of Inf class
    #
    def ShowInf(self):
        print TAB_SECTION_START + TAB_INF_DEFINES + TAB_SECTION_END
        printDict(self.Defines.DefinesDictionary)

        for key in self.KeyList:
            for arch in DataType.ARCH_LIST_FULL:
                Command = "printList(TAB_SECTION_START + '" + \
                          key + DataType.TAB_SPLIT + arch + \
                          "' + TAB_SECTION_END, self.Contents[arch]." + key + ')'
                eval(Command)
        print ""
    
    ## Show detailed information of Module
    #
    # Print all members and their values of Module class
    #
    def ShowModule(self):
        M = self.Module
        print 'Filename =', M.Header.FileName
        print 'FullPath =', M.Header.FullPath
        print 'BaseName =', M.Header.Name
        print 'Guid =', M.Header.Guid
        print 'Version =', M.Header.Version
        print 'InfVersion =', M.Header.InfVersion
        print 'EfiSpecificationVersion =', M.Header.EfiSpecificationVersion
        print 'EdkReleaseVersion =', M.Header.EdkReleaseVersion                
        print 'ModuleType =', M.Header.ModuleType
        print 'BinaryModule =', M.Header.BinaryModule
        print 'ComponentType =', M.Header.ComponentType
        print 'MakefileName =', M.Header.MakefileName
        print 'BuildNumber =', M.Header.BuildNumber
        print 'BuildType =', M.Header.BuildType
        print 'FfsExt =', M.Header.FfsExt
        print 'FvExt =', M.Header.FvExt
        print 'SourceFv =', M.Header.SourceFv
        print 'PcdIsDriver =', M.Header.PcdIsDriver
        print 'TianoR8FlashMap_h =', M.Header.TianoR8FlashMap_h
        print 'Shadow =', M.Header.Shadow
        print 'LibraryClass =', M.Header.LibraryClass
        for Item in M.Header.LibraryClass:
            print Item.LibraryClass, DataType.TAB_VALUE_SPLIT.join(Item.SupModuleList)
        print 'CustomMakefile =', M.Header.CustomMakefile
        for Item in self.Module.ExternImages:
            print 'Entry_Point = %s, UnloadImage = %s' % (Item.ModuleEntryPoint, Item.ModuleUnloadImage)
        for Item in self.Module.ExternLibraries:
            print 'Constructor = %s, Destructor = %s' % (Item.Constructor, Item.Destructor)
        print 'Define =', M.Header.Define
        print 'Specification =', M.Header.Specification
        print '\nBuildOptions =', M.BuildOptions
        for Item in M.BuildOptions:
            print Item.ToolChainFamily, Item.ToolChain, Item.Option, Item.SupArchList
        print '\nIncludes =', M.Includes
        for Item in M.Includes:
            print Item.FilePath, Item.SupArchList
        print '\nLibraries =', M.Libraries
        for Item in M.Libraries:
            print Item.Library, Item.SupArchList
        print '\nLibraryClasses =', M.LibraryClasses
        for Item in M.LibraryClasses:
            print Item.LibraryClass, Item.RecommendedInstance, Item.FeatureFlag, Item.SupModuleList, Item.SupArchList, Item.Define
        print '\nPackageDependencies =', M.PackageDependencies
        for Item in M.PackageDependencies:
            print Item.FilePath, Item.SupArchList, Item.Define
        print '\nNmake =', M.Nmake
        for Item in M.Nmake:
            print Item.Name, Item.Value, Item.SupArchList
        print '\nPcds =', M.PcdCodes
        for Item in M.PcdCodes:
            print '\tCName=',Item.CName, 'TokenSpaceGuidCName=', Item.TokenSpaceGuidCName, 'DefaultValue=', Item.DefaultValue, 'ItemType=', Item.ItemType, Item.SupArchList
        print '\nSources =', M.Sources
        for Source in M.Sources:
            print Source.SourceFile, 'Fam=', Source.ToolChainFamily, 'Pcd=', Source.FeatureFlag, 'Tag=', Source.TagName, 'ToolCode=', Source.ToolCode, Source.SupArchList
        print '\nUserExtensions =', M.UserExtensions
        for UserExtension in M.UserExtensions:
            print UserExtension.UserID, UserExtension.Identifier,UserExtension.Content
        print '\nGuids =', M.Guids
        for Item in M.Guids:
            print Item.CName, Item.SupArchList
        print '\nProtocols =', M.Protocols
        for Item in M.Protocols:
            print Item.CName, Item.SupArchList
        print '\nPpis =', M.Ppis
        for Item in M.Ppis:
            print Item.CName, Item.SupArchList
        print '\nDepex =', M.Depex
        for Item in M.Depex:
            print Item.Depex, Item.SupArchList, Item.Define
        print '\nBinaries =', M.Binaries
        for Binary in M.Binaries:
            print 'Type=', Binary.FileType, 'Target=', Binary.Target, 'Name=', Binary.BinaryFile, 'FeatureFlag=', Binary.FeatureFlag, 'SupArchList=', Binary.SupArchList

##
#
# This acts like the main() function for the script, unless it is 'import'ed into another
# script.
#
if __name__ == '__main__':
    W = os.getenv('WORKSPACE')
    F = os.path.join(W, 'MdeModulePkg/Application/HelloWorld/HelloWorld.inf')
    P = Inf(os.path.normpath(F), True, True, W)
    P.ShowModule()
