import { CaseFile, CaseFileAPIData } from "@/models/CaseFile";
import { Initiation } from "@/models/Initiation";
import { StaffUser } from "@/models/Staff";
import { OnSuccessType, request } from "@/utils/axiosUtils";
import { UNAPPROVED_PROJECT_ABBREVIATION, UNAPPROVED_PROJECT_ID } from "@/utils/constants";
import { useMutation, useQuery } from "@tanstack/react-query";

const fetchCaseFiles = (projectId?: number): Promise<CaseFile[]> => {
  return request({ url: "/case-files", params: { project_id: projectId } });
};

const fetchCaseFile = (caseFileNumber: string): Promise<CaseFile> => {
  return request({ url: `/case-files/case-file-numbers/${caseFileNumber}` });
};

const fetchOfficers = (caseFileId: number): Promise<StaffUser[]> => {
  return request({ url: `/case-files/${caseFileId}/officers` });
};

const fetchInitiations = (): Promise<Initiation[]> => {
  return request({ url: "/case-files/initiation-options" });
};

const createCaseFile = (caseFile: CaseFileAPIData) => {
  return request({ url: "/case-files", method: "post", data: caseFile });
};

const updateCaseFile = ({
  id,
  caseFile,
}: {
  id: number;
  caseFile: CaseFileAPIData;
}) => {
  return request({ url: `/case-files/${id}`, method: "patch", data: caseFile });
};

export const useCaseFilesData = () => {
  return useQuery({
    queryKey: ["case-files"],
    queryFn: () => fetchCaseFiles(),
  });
};

export const useCaseFileByNumber = (caseFileNumber: string) => {
  return useQuery({
    queryKey: ["case-file", caseFileNumber],
    queryFn: async () => {
      const caseFile = await fetchCaseFile(caseFileNumber);
      const officers = await fetchOfficers(caseFile?.id);
      if (caseFile.project.abbreviation === UNAPPROVED_PROJECT_ABBREVIATION) {
        caseFile.project.id = UNAPPROVED_PROJECT_ID;
        delete caseFile.project.abbreviation;
      }
      return { ...caseFile, officers };
    },
    enabled: !!caseFileNumber,
  });
};

export const useOfficersByCaseFileId = (caseFileId: number) => {
  return useQuery({
    queryKey: ["officers", caseFileId],
    queryFn: () => fetchOfficers(caseFileId),
    enabled: !!caseFileId,
  });
};

export const useCaseFilesByProjectId = (projectId: number) => {
  return useQuery({
    queryKey: ["case-files-by-projectId", projectId],
    queryFn: () => fetchCaseFiles(projectId),
    enabled: !!projectId,
  });
};

export const useInitiationsData = () => {
  return useQuery({
    queryKey: ["case-files-initiations"],
    queryFn: fetchInitiations,
  });
};

export const useCreateCaseFile = (onSuccess: OnSuccessType) => {
  return useMutation({ mutationFn: createCaseFile, onSuccess });
};

export const useUpdateCaseFile = (onSuccess: OnSuccessType) => {
  return useMutation({ mutationFn: updateCaseFile, onSuccess });
};
