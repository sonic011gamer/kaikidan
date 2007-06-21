/*++

Copyright (c) 2004, Intel Corporation                                                         
All rights reserved. This program and the accompanying materials                          
are licensed and made available under the terms and conditions of the BSD License         
which accompanies this distribution.  The full text of the license may be found at        
http://opensource.org/licenses/bsd-license.php                                            
                                                                                          
THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,                     
WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.             

Module Name:
  
  GenFvInternalLib.h

Abstract:

  This file contains describes the public interfaces to the GenFvImage Library.
  The basic purpose of the library is to create Firmware Volume images.

--*/

#ifndef _EFI_GEN_FV_INTERNAL_LIB_H
#define _EFI_GEN_FV_INTERNAL_LIB_H

//
// Include files
//
#include <stdlib.h>

#include <Common/UefiBaseTypes.h>
#include <Common/MultiPhase.h>

#include <Common/FirmwareVolumeImageFormat.h>
#include <Common/PiFirmwareVolumeHeader.h>
#include <Common/PiFirmwareFileSystem.h>
#include <Guid/PiFirmwareFileSystem.h>

#include <Common/EfiImage.h>

#include "CommonLib.h"
#include "ParseInf.h"

//
// Private data declarations
//

//
// Different file separater for Linux and Windows
//
#ifdef __GNUC__
#define FILE_SEP_CHAR '/'
#define FILE_SEP_STRING "/"
#else
#define FILE_SEP_CHAR '\\'
#define FILE_SEP_STRING "\\"
#endif

//
// The maximum number of block map entries supported by the library
//
#define MAX_NUMBER_OF_FV_BLOCKS         100

//
// The maximum number of files in the FV supported by the library
//
#define MAX_NUMBER_OF_FILES_IN_FV       1000
#define MAX_NUMBER_OF_COMPONENTS_IN_FV  10
#define EFI_FFS_FILE_HEADER_ALIGNMENT   8

//
// INF file strings
//
#define OPTIONS_SECTION_STRING            "[options]"
#define ATTRIBUTES_SECTION_STRING         "[attributes]"
#define FILES_SECTION_STRING              "[files]"
#define COMPONENT_SECTION_STRING          "[components]"

//
// Options section
//
#define EFI_FV_BASE_ADDRESS_STRING        "EFI_BASE_ADDRESS"
#define EFI_FV_FILE_NAME_STRING           "EFI_FILE_NAME"
#define EFI_SYM_FILE_NAME_STRING          "EFI_SYM_FILE_NAME"
#define EFI_NUM_BLOCKS_STRING             "EFI_NUM_BLOCKS"
#define EFI_BLOCK_SIZE_STRING             "EFI_BLOCK_SIZE"
#define EFI_FV_GUID_STRING                "EFI_FV_GUID"

//
// Attributes section
//
#define EFI_FVB2_READ_DISABLED_CAP_STRING  "EFI_READ_DISABLED_CAP"
#define EFI_FVB2_READ_ENABLED_CAP_STRING   "EFI_READ_ENABLED_CAP"
#define EFI_FVB2_READ_STATUS_STRING        "EFI_READ_STATUS"

#define EFI_FVB2_WRITE_DISABLED_CAP_STRING "EFI_WRITE_DISABLED_CAP"
#define EFI_FVB2_WRITE_ENABLED_CAP_STRING  "EFI_WRITE_ENABLED_CAP"
#define EFI_FVB2_WRITE_STATUS_STRING       "EFI_WRITE_STATUS"

#define EFI_FVB2_LOCK_CAP_STRING           "EFI_LOCK_CAP"
#define EFI_FVB2_LOCK_STATUS_STRING        "EFI_LOCK_STATUS"

#define EFI_FVB2_STICKY_WRITE_STRING       "EFI_STICKY_WRITE"
#define EFI_FVB2_MEMORY_MAPPED_STRING      "EFI_MEMORY_MAPPED"
#define EFI_FVB2_ERASE_POLARITY_STRING     "EFI_ERASE_POLARITY"

#define EFI_FVB2_READ_LOCK_CAP_STRING      "EFI_READ_LOCK_CAP"
#define EFI_FVB2_READ_LOCK_STATUS_STRING   "EFI_READ_LOCK_STATUS"
#define EFI_FVB2_WRITE_LOCK_CAP_STRING     "EFI_WRITE_LOCK_CAP"
#define EFI_FVB2_WRITE_LOCK_STATUS_STRING  "EFI_WRITE_LOCK_STATUS"

#define EFI_FVB2_ALIGNMENT_1_STRING       "EFI_FVB2_ALIGNMENT_1"   
#define EFI_FVB2_ALIGNMENT_2_STRING       "EFI_FVB2_ALIGNMENT_2"   
#define EFI_FVB2_ALIGNMENT_4_STRING       "EFI_FVB2_ALIGNMENT_4"   
#define EFI_FVB2_ALIGNMENT_8_STRING       "EFI_FVB2_ALIGNMENT_8"   
#define EFI_FVB2_ALIGNMENT_16_STRING      "EFI_FVB2_ALIGNMENT_16"  
#define EFI_FVB2_ALIGNMENT_32_STRING      "EFI_FVB2_ALIGNMENT_32"  
#define EFI_FVB2_ALIGNMENT_64_STRING      "EFI_FVB2_ALIGNMENT_64"  
#define EFI_FVB2_ALIGNMENT_128_STRING     "EFI_FVB2_ALIGNMENT_128" 
#define EFI_FVB2_ALIGNMENT_256_STRING     "EFI_FVB2_ALIGNMENT_256" 
#define EFI_FVB2_ALIGNMENT_512_STRING     "EFI_FVB2_ALIGNMENT_512" 
#define EFI_FVB2_ALIGNMENT_1K_STRING      "EFI_FVB2_ALIGNMENT_1K"  
#define EFI_FVB2_ALIGNMENT_2K_STRING      "EFI_FVB2_ALIGNMENT_2K"  
#define EFI_FVB2_ALIGNMENT_4K_STRING      "EFI_FVB2_ALIGNMENT_4K"  
#define EFI_FVB2_ALIGNMENT_8K_STRING      "EFI_FVB2_ALIGNMENT_8K"  
#define EFI_FVB2_ALIGNMENT_16K_STRING     "EFI_FVB2_ALIGNMENT_16K" 
#define EFI_FVB2_ALIGNMENT_32K_STRING     "EFI_FVB2_ALIGNMENT_32K" 
#define EFI_FVB2_ALIGNMENT_64K_STRING     "EFI_FVB2_ALIGNMENT_64K" 
#define EFI_FVB2_ALIGNMENT_128K_STRING    "EFI_FVB2_ALIGNMENT_128K"
#define EFI_FVB2_ALIGNMENT_256K_STRING    "EFI_FVB2_ALIGNMENT_256K"
#define EFI_FVB2_ALIGNMNET_512K_STRING    "EFI_FVB2_ALIGNMENT_512K"
#define EFI_FVB2_ALIGNMENT_1M_STRING      "EFI_FVB2_ALIGNMENT_1M"  
#define EFI_FVB2_ALIGNMENT_2M_STRING      "EFI_FVB2_ALIGNMENT_2M"  
#define EFI_FVB2_ALIGNMENT_4M_STRING      "EFI_FVB2_ALIGNMENT_4M"  
#define EFI_FVB2_ALIGNMENT_8M_STRING      "EFI_FVB2_ALIGNMENT_8M"  
#define EFI_FVB2_ALIGNMENT_16M_STRING     "EFI_FVB2_ALIGNMENT_16M" 
#define EFI_FVB2_ALIGNMENT_32M_STRING     "EFI_FVB2_ALIGNMENT_32M" 
#define EFI_FVB2_ALIGNMENT_64M_STRING     "EFI_FVB2_ALIGNMENT_64M" 
#define EFI_FVB2_ALIGNMENT_128M_STRING    "EFI_FVB2_ALIGNMENT_128M"
#define EFI_FVB2_ALIGNMENT_256M_STRING    "EFI_FVB2_ALIGNMENT_256M"
#define EFI_FVB2_ALIGNMENT_512M_STRING    "EFI_FVB2_ALIGNMENT_512M"
#define EFI_FVB2_ALIGNMENT_1G_STRING      "EFI_FVB2_ALIGNMENT_1G"  
#define EFI_FVB2_ALIGNMENT_2G_STRING      "EFI_FVB2_ALIGNMENT_2G"  

//
// Component sections
//
#define EFI_NV_VARIABLE_STRING    "EFI_NV_VARIABLE"
#define EFI_NV_EVENT_LOG_STRING   "EFI_NV_EVENT_LOG"
#define EFI_NV_FTW_WORKING_STRING "EFI_NV_FTW_WORKING"
#define EFI_NV_FTW_SPARE_STRING   "EFI_NV_FTW_SPARE"

//
// File sections
//
#define EFI_FILE_NAME_STRING      "EFI_FILE_NAME"

#define ONE_STRING                "1"
#define ZERO_STRING               "0"
#define TRUE_STRING               "TRUE"
#define FALSE_STRING              "FALSE"
#define NULL_STRING               "NULL"

//
// Defines to calculate the offset for PEI CORE entry points
//
#define IA32_PEI_CORE_ENTRY_OFFSET    0x20

//
// Defines to calculate the FIT table
//
#define IPF_FIT_ADDRESS_OFFSET        0x20

//
// Defines to calculate the offset for SALE_ENTRY
//
#define IPF_SALE_ENTRY_ADDRESS_OFFSET 0x18

//
// Symbol file definitions, current max size if 512K
//
#define SYMBOL_FILE_SIZE              0x80000

#define FV_IMAGES_TOP_ADDRESS         0x100000000ULL

//
// Following definition is used for FIT in IPF
//
#define COMP_TYPE_FIT_PEICORE 0x10
#define COMP_TYPE_FIT_UNUSED  0x7F

#define FIT_TYPE_MASK         0x7F
#define CHECKSUM_BIT_MASK     0x80

//
// Private data types
//
//
// Component information
//
typedef struct {
  UINTN Size;
  CHAR8 ComponentName[_MAX_PATH];
} COMPONENT_INFO;

//
// FV information holder
//
typedef struct {
  EFI_PHYSICAL_ADDRESS    BaseAddress;
  EFI_GUID                FvGuid;
  UINTN                   Size;
  CHAR8                   FvName[_MAX_PATH];
  EFI_FV_BLOCK_MAP_ENTRY  FvBlocks[MAX_NUMBER_OF_FV_BLOCKS];
  EFI_FVB_ATTRIBUTES      FvAttributes;
  CHAR8                   FvFiles[MAX_NUMBER_OF_FILES_IN_FV][_MAX_PATH];
} FV_INFO;

#pragma pack(1)

typedef struct {
  UINT64  CompAddress;
  UINT32  CompSize;
  UINT16  CompVersion;
  UINT8   CvAndType;
  UINT8   CheckSum;
} FIT_TABLE;

#pragma pack()

//
// Local function prototypes
//
EFI_STATUS
ParseFvInf (
  IN  MEMORY_FILE  *InfFile,
  OUT FV_INFO      *FvInfo
  )
;

EFI_STATUS
UpdatePeiCoreEntryInFit (
  IN FIT_TABLE     *FitTablePtr,
  IN UINT64        PeiCorePhysicalAddress
  )
/*++

Routine Description:

  This function is used to update the Pei Core address in FIT, this can be used by Sec core to pass control from
  Sec to Pei Core

Arguments:

  FitTablePtr             - The pointer of FIT_TABLE.
  PeiCorePhysicalAddress  - The address of Pei Core entry.

Returns:

  EFI_SUCCESS             - The PEI_CORE FIT entry was updated successfully.
  EFI_NOT_FOUND           - Not found the PEI_CORE FIT entry.

--*/
;

VOID
UpdateFitCheckSum (
  IN FIT_TABLE   *FitTablePtr
  )
/*++

Routine Description:

  This function is used to update the checksum for FIT.


Arguments:

  FitTablePtr             - The pointer of FIT_TABLE.

Returns:

  None.

--*/
;

EFI_STATUS
GetPe32Info (
  IN UINT8                  *Pe32,
  OUT UINT32                *EntryPoint,
  OUT UINT32                *BaseOfCode,
  OUT UINT16                *MachineType
  );

//
// Exported function prototypes
//
EFI_STATUS
GenerateFvImage (
  IN CHAR8                *InfFileImage,
  IN UINTN                InfFileSize,
  IN CHAR8                *FvFileName,  
  IN EFI_PHYSICAL_ADDRESS XipBaseAddress
  )
/*++

Routine Description:

  This is the main function which will be called from application.

Arguments:

  InfFileImage   Buffer containing the INF file contents.
  InfFileSize    Size of the contents of the InfFileImage buffer.
  FvFileName     Requested name for the FV file.
  XipBaseAddress BaseAddress is to be rebased.
    
Returns:
 
  EFI_SUCCESS             Function completed successfully.
  EFI_OUT_OF_RESOURCES    Could not allocate required resources.
  EFI_ABORTED             Error encountered.
  EFI_INVALID_PARAMETER   A required parameter was NULL.

--*/
;

#endif
