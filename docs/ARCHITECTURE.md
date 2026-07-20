# DMJ Dataset Builder Architecture

```
Raw Dataset
      │
      ▼
Downloader
      │
      ▼
Importer Registry
      │
      ▼
Converter
      │
      ▼
Metadata Enrichment
      │
      ▼
Validation
      │
      ▼
Statistics
      │
      ▼
Merge
      │
      ▼
Final Dataset
```

The architecture is designed to make adding new dataset importers straightforward while keeping the processing pipeline modular.