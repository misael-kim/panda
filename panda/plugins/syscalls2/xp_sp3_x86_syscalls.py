syscalls = [
    [
    'NtAcceptConnectPort', # 0x0
    'NtAccessCheck', # 0x1
    'NtAccessCheckAndAuditAlarm', # 0x2
    'NtAccessCheckByType', # 0x3
    'NtAccessCheckByTypeAndAuditAlarm', # 0x4
    'NtAccessCheckByTypeResultList', # 0x5
    'NtAccessCheckByTypeResultListAndAuditAlarm', # 0x6
    'NtAccessCheckByTypeResultListAndAuditAlarmByHandle', # 0x7
    'NtAddAtom', # 0x8
    'NtEnumerateBootEntries', # 0x9
    'NtAdjustGroupsToken', # 0xa
    'NtAdjustPrivilegesToken', # 0xb
    'NtAlertResumeThread', # 0xc
    'NtAlertThread', # 0xd
    'NtAllocateLocallyUniqueId', # 0xe
    'NtAllocateUserPhysicalPages', # 0xf
    'NtAllocateUuids', # 0x10
    'NtAllocateVirtualMemory', # 0x11
    'NtAreMappedFilesTheSame', # 0x12
    'NtAssignProcessToJobObject', # 0x13
    'NtCallbackReturn', # 0x14
    'NtModifyBootEntry', # 0x15
    'NtCancelIoFile', # 0x16
    'NtCancelTimer', # 0x17
    'NtClearEvent', # 0x18
    'NtClose', # 0x19
    'NtCloseObjectAuditAlarm', # 0x1a
    'NtCompactKeys', # 0x1b
    'NtCompareTokens', # 0x1c
    'NtCompleteConnectPort', # 0x1d
    'NtCompressKey', # 0x1e
    'NtConnectPort', # 0x1f
    'NtContinue', # 0x20
    'NtCreateDebugObject', # 0x21
    'NtCreateDirectoryObject', # 0x22
    'NtCreateEvent', # 0x23
    'NtCreateEventPair', # 0x24
    'NtCreateFile', # 0x25
    'NtCreateIoCompletion', # 0x26
    'NtCreateJobObject', # 0x27
    'NtCreateJobSet', # 0x28
    'NtCreateKey', # 0x29
    'NtCreateMailslotFile', # 0x2a
    'NtCreateMutant', # 0x2b
    'NtCreateNamedPipeFile', # 0x2c
    'NtCreatePagingFile', # 0x2d
    'NtCreatePort', # 0x2e
    'NtCreateProcess', # 0x2f
    'NtCreateProcessEx', # 0x30
    'NtCreateProfile', # 0x31
    'NtCreateSection', # 0x32
    'NtCreateSemaphore', # 0x33
    'NtCreateSymbolicLinkObject', # 0x34
    'NtCreateThread', # 0x35
    'NtCreateTimer', # 0x36
    'NtCreateToken', # 0x37
    'NtCreateWaitablePort', # 0x38
    'NtDebugActiveProcess', # 0x39
    'NtDebugContinue', # 0x3a
    'NtDelayExecution', # 0x3b
    'NtDeleteAtom', # 0x3c
    'NtDeleteFile', # 0x3e
    'NtDeleteKey', # 0x3f
    'NtDeleteObjectAuditAlarm', # 0x40
    'NtDeleteValueKey', # 0x41
    'NtDeviceIoControlFile', # 0x42
    'NtDisplayString', # 0x43
    'NtDuplicateObject', # 0x44
    'NtDuplicateToken', # 0x45
    'NtEnumerateKey', # 0x47
    'NtEnumerateSystemEnvironmentValuesEx', # 0x48
    'NtEnumerateValueKey', # 0x49
    'NtExtendSection', # 0x4a
    'NtFilterToken', # 0x4b
    'NtFindAtom', # 0x4c
    'NtFlushBuffersFile', # 0x4d
    'NtFlushInstructionCache', # 0x4e
    'NtFlushKey', # 0x4f
    'NtFlushVirtualMemory', # 0x50
    'NtFlushWriteBuffer', # 0x51
    'NtFreeUserPhysicalPages', # 0x52
    'NtFreeVirtualMemory', # 0x53
    'NtFsControlFile', # 0x54
    'NtGetContextThread', # 0x55
    'NtGetDevicePowerState', # 0x56
    'NtGetPlugPlayEvent', # 0x57
    'NtGetWriteWatch', # 0x58
    'NtImpersonateAnonymousToken', # 0x59
    'NtImpersonateClientOfPort', # 0x5a
    'NtImpersonateThread', # 0x5b
    'NtInitializeRegistry', # 0x5c
    'NtInitiatePowerAction', # 0x5d
    'NtIsProcessInJob', # 0x5e
    'NtIsSystemResumeAutomatic', # 0x5f
    'NtListenPort', # 0x60
    'NtLoadDriver', # 0x61
    'NtLoadKey', # 0x62
    'NtLoadKey2', # 0x63
    'NtLockFile', # 0x64
    'NtLockProductActivationKeys', # 0x65
    'NtLockRegistryKey', # 0x66
    'NtLockVirtualMemory', # 0x67
    'NtMakePermanentObject', # 0x68
    'NtMakeTemporaryObject', # 0x69
    'NtMapUserPhysicalPages', # 0x6a
    'NtMapUserPhysicalPagesScatter', # 0x6b
    'NtMapViewOfSection', # 0x6c
    'NtNotifyChangeDirectoryFile', # 0x6e
    'NtNotifyChangeKey', # 0x6f
    'NtNotifyChangeMultipleKeys', # 0x70
    'NtOpenDirectoryObject', # 0x71
    'NtOpenEvent', # 0x72
    'NtOpenEventPair', # 0x73
    'NtOpenFile', # 0x74
    'NtOpenIoCompletion', # 0x75
    'NtOpenJobObject', # 0x76
    'NtOpenKey', # 0x77
    'NtOpenMutant', # 0x78
    'NtOpenObjectAuditAlarm', # 0x79
    'NtOpenProcess', # 0x7a
    'NtOpenProcessToken', # 0x7b
    'NtOpenProcessTokenEx', # 0x7c
    'NtOpenSection', # 0x7d
    'NtOpenSemaphore', # 0x7e
    'NtOpenSymbolicLinkObject', # 0x7f
    'NtOpenThread', # 0x80
    'NtOpenThreadToken', # 0x81
    'NtOpenThreadTokenEx', # 0x82
    'NtOpenTimer', # 0x83
    'NtPlugPlayControl', # 0x84
    'NtPowerInformation', # 0x85
    'NtPrivilegeCheck', # 0x86
    'NtPrivilegeObjectAuditAlarm', # 0x87
    'NtPrivilegedServiceAuditAlarm', # 0x88
    'NtProtectVirtualMemory', # 0x89
    'NtPulseEvent', # 0x8a
    'NtQueryAttributesFile', # 0x8b
    'NtQueryDebugFilterState', # 0x8e
    'NtQueryDefaultLocale', # 0x8f
    'NtQueryDefaultUILanguage', # 0x90
    'NtQueryDirectoryFile', # 0x91
    'NtQueryDirectoryObject', # 0x92
    'NtQueryEaFile', # 0x93
    'NtQueryEvent', # 0x94
    'NtQueryFullAttributesFile', # 0x95
    'NtQueryInformationAtom', # 0x96
    'NtQueryInformationFile', # 0x97
    'NtQueryInformationJobObject', # 0x98
    'NtQueryInformationPort', # 0x99
    'NtQueryInformationProcess', # 0x9a
    'NtQueryInformationThread', # 0x9b
    'NtQueryInformationToken', # 0x9c
    'NtQueryInstallUILanguage', # 0x9d
    'NtQueryIntervalProfile', # 0x9e
    'NtQueryIoCompletion', # 0x9f
    'NtQueryKey', # 0xa0
    'NtQueryMultipleValueKey', # 0xa1
    'NtQueryMutant', # 0xa2
    'NtQueryObject', # 0xa3
    'NtQueryOpenSubKeys', # 0xa4
    'NtQueryPerformanceCounter', # 0xa5
    'NtQueryQuotaInformationFile', # 0xa6
    'NtQuerySection', # 0xa7
    'NtQuerySecurityObject', # 0xa8
    'NtQuerySemaphore', # 0xa9
    'NtQuerySymbolicLinkObject', # 0xaa
    'NtQuerySystemEnvironmentValue', # 0xab
    'NtQuerySystemEnvironmentValueEx', # 0xac
    'NtQuerySystemInformation', # 0xad
    'NtQuerySystemTime', # 0xae
    'NtQueryTimer', # 0xaf
    'NtQueryTimerResolution', # 0xb0
    'NtQueryValueKey', # 0xb1
    'NtQueryVirtualMemory', # 0xb2
    'NtQueryVolumeInformationFile', # 0xb3
    'NtQueueApcThread', # 0xb4
    'NtRaiseException', # 0xb5
    'NtRaiseHardError', # 0xb6
    'NtReadFile', # 0xb7
    'NtReadFileScatter', # 0xb8
    'NtReadRequestData', # 0xb9
    'NtReadVirtualMemory', # 0xba
    'NtRegisterThreadTerminatePort', # 0xbb
    'NtReleaseMutant', # 0xbc
    'NtReleaseSemaphore', # 0xbd
    'NtRemoveIoCompletion', # 0xbe
    'NtRemoveProcessDebug', # 0xbf
    'NtRenameKey', # 0xc0
    'NtReplaceKey', # 0xc1
    'NtReplyPort', # 0xc2
    'NtReplyWaitReceivePort', # 0xc3
    'NtReplyWaitReceivePortEx', # 0xc4
    'NtReplyWaitReplyPort', # 0xc5
    'NtRequestDeviceWakeup', # 0xc6
    'NtRequestPort', # 0xc7
    'NtRequestWaitReplyPort', # 0xc8
    'NtRequestWakeupLatency', # 0xc9
    'NtResetEvent', # 0xca
    'NtResetWriteWatch', # 0xcb
    'NtRestoreKey', # 0xcc
    'NtResumeProcess', # 0xcd
    'NtResumeThread', # 0xce
    'NtSaveKey', # 0xcf
    'NtSaveKeyEx', # 0xd0
    'NtSaveMergedKeys', # 0xd1
    'NtSecureConnectPort', # 0xd2
    'NtSetContextThread', # 0xd5
    'NtSetDebugFilterState', # 0xd6
    'NtSetDefaultHardErrorPort', # 0xd7
    'NtSetDefaultLocale', # 0xd8
    'NtSetDefaultUILanguage', # 0xd9
    'NtSetEaFile', # 0xda
    'NtSetEvent', # 0xdb
    'NtSetEventBoostPriority', # 0xdc
    'NtSetHighEventPair', # 0xdd
    'NtSetHighWaitLowEventPair', # 0xde
    'NtSetInformationDebugObject', # 0xdf
    'NtSetInformationFile', # 0xe0
    'NtSetInformationJobObject', # 0xe1
    'NtSetInformationKey', # 0xe2
    'NtSetInformationObject', # 0xe3
    'NtSetInformationProcess', # 0xe4
    'NtSetInformationThread', # 0xe5
    'NtSetInformationToken', # 0xe6
    'NtSetIntervalProfile', # 0xe7
    'NtSetIoCompletion', # 0xe8
    'NtSetLdtEntries', # 0xe9
    'NtSetLowEventPair', # 0xea
    'NtSetLowWaitHighEventPair', # 0xeb
    'NtSetQuotaInformationFile', # 0xec
    'NtSetSecurityObject', # 0xed
    'NtSetSystemEnvironmentValue', # 0xee
    'NtSetSystemInformation', # 0xf0
    'NtSetSystemPowerState', # 0xf1
    'NtSetSystemTime', # 0xf2
    'NtSetThreadExecutionState', # 0xf3
    'NtSetTimer', # 0xf4
    'NtSetTimerResolution', # 0xf5
    'NtSetUuidSeed', # 0xf6
    'NtSetValueKey', # 0xf7
    'NtSetVolumeInformationFile', # 0xf8
    'NtShutdownSystem', # 0xf9
    'NtSignalAndWaitForSingleObject', # 0xfa
    'NtStartProfile', # 0xfb
    'NtStopProfile', # 0xfc
    'NtSuspendProcess', # 0xfd
    'NtSuspendThread', # 0xfe
    'NtSystemDebugControl', # 0xff
    'NtTerminateJobObject', # 0x100
    'NtTerminateProcess', # 0x101
    'NtTerminateThread', # 0x102
    'NtTestAlert', # 0x103
    'NtTraceEvent', # 0x104
    'NtTranslateFilePath', # 0x105
    'NtUnloadDriver', # 0x106
    'NtUnloadKey', # 0x107
    'NtUnloadKeyEx', # 0x108
    'NtUnlockFile', # 0x109
    'NtUnlockVirtualMemory', # 0x10a
    'NtUnmapViewOfSection', # 0x10b
    'NtVdmControl', # 0x10c
    'NtWaitForDebugEvent', # 0x10d
    'NtWaitForMultipleObjects', # 0x10e
    'NtWaitForSingleObject', # 0x10f
    'NtWaitHighEventPair', # 0x110
    'NtWaitLowEventPair', # 0x111
    'NtWriteFile', # 0x112
    'NtWriteFileGather', # 0x113
    'NtWriteRequestData', # 0x114
    'NtWriteVirtualMemory', # 0x115
    'NtYieldExecution', # 0x116
    'NtCreateKeyedEvent', # 0x117
    'NtOpenKeyedEvent', # 0x118
    'NtReleaseKeyedEvent', # 0x119
    'NtWaitForKeyedEvent', # 0x11a
    'NtQueryPortInformationProcess', # 0x11b
    ]
]
