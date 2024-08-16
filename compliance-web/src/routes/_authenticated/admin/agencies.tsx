import MasterDataTable from '@/components/Shared/MasterDataTable/MasterDataTable';
import { searchFilter } from '@/components/Shared/MasterDataTable/utils';
import { useAgenciesData } from '@/hooks/useAgencies';
import { Agency } from '@/models/Agency';
import { EditOutlined, DeleteOutlineRounded, AddRounded } from '@mui/icons-material';
import { Box, IconButton, Typography, Button } from '@mui/material';
import { createFileRoute } from '@tanstack/react-router'
import { BCDesignTokens } from 'epic.theme';
import { MRT_ColumnDef } from 'material-react-table';
import { useMemo } from 'react';

export const Route = createFileRoute('/_authenticated/admin/agencies')({
  component: Agencies
})

function Agencies() {
  const { data: agenciesList, isLoading } = useAgenciesData();

  const columns = useMemo<MRT_ColumnDef<Agency>[]>(
    () => [
      {
        accessorKey: "name",
        header: "Name",
        sortingFn: "sortFn",
        filterFn: searchFilter,
      },
      {
        accessorKey: "abbreviation",
        header: "Abbreviation",
        sortingFn: "sortFn",
        filterFn: searchFilter,
      },
    ],
    []
  );

  const handleOpenModal = () => {
    //TODO: OPEN MODAL
  };

  const handleDelete = (id: number) => {
    // TODO: DELETE
    // eslint-disable-next-line no-console
    console.log(id);
  };

  const handleEdit = (id: number) => {
    // TODO: EDIT
    // eslint-disable-next-line no-console
    console.log(id);
  };

  return (
    <>
      <MasterDataTable
        columns={columns}
        data={agenciesList ?? []}
        initialState={{
          sorting: [
            {
              id: "name",
              desc: false,
            },
          ],
        }}
        state={{
          isLoading: isLoading,
          showGlobalFilter: true,
        }}
        enableRowActions={true}
        renderRowActions={({ row }) => (
          <Box gap={".25rem"} display={"flex"}>
            <IconButton
              aria-label="edit"
              onClick={() => handleEdit(row.original.id)}
            >
              <EditOutlined />
            </IconButton>
            <IconButton
              aria-label="delete"
              onClick={() => handleDelete(row.original.id)}
            >
              <DeleteOutlineRounded />
            </IconButton>
          </Box>
        )}
        renderTopToolbarCustomActions={() => (
          <Box
            sx={{
              width: "100%",
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <Typography
              variant="h5"
              sx={{ color: BCDesignTokens.typographyColorLink }}
            >
              Agencies
            </Typography>
            <Button
              startIcon={<AddRounded />}
              onClick={() => handleOpenModal()}
            >
              Agency
            </Button>
          </Box>
        )}
      />
    </>
  );
}
