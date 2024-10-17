import { Attendance } from "@/models/Attendance";
import { Initiation } from "@/models/Initiation";
import { Inspection, InspectionAPIData } from "@/models/Inspection";
import { IRStatus } from "@/models/IRStatus";
import { IRType } from "@/models/IRType";
import { ProjectStatus } from "@/models/ProjectStatus";
import { StaffUser } from "@/models/Staff";
import { OnSuccessType, request } from "@/utils/axiosUtils";
import { UNAPPROVED_PROJECT_ABBREVIATION } from "@/utils/constants";
import { UNAPPROVED_PROJECT_ID } from "@/utils/constants";
import { useMutation, useQuery } from "@tanstack/react-query";

const fetchIRTypes = (): Promise<IRType[]> => {
  return request({ url: "/inspections/type-options" });
};

const fetchInitiations = (): Promise<Initiation[]> => {
  return request({ url: "/inspections/initiation-options" });
};

const fetchIRStatuses = (): Promise<IRStatus[]> => {
  return request({ url: "/inspections/ir-status-options" });
};

const fetchAttendanceOptions = (): Promise<Attendance[]> => {
  return request({ url: "/inspections/attendance-options" });
};

const fetchProjectStatuses = (): Promise<ProjectStatus[]> => {
  return request({ url: "/project-status-options" });
};

const fetchInspections = (): Promise<Inspection[]> => {
  return request({ url: "/inspections" });
};

const fetchInspection = (inspectionNumber: string): Promise<Inspection> => {
  return request({ url: `/inspections/ir-numbers/${inspectionNumber}` });
};

const fetchOfficers = (inspectionId: number): Promise<StaffUser[]> => {
  return request({ url: `/inspections/${inspectionId}/officers` });
};

const createInspection = (inspection: InspectionAPIData) => {
  return request({ url: "/inspections", method: "post", data: inspection });
};

export const useIRTypesData = () => {
  return useQuery({
    queryKey: ["ir-types"],
    queryFn: fetchIRTypes,
  });
};

export const useInitiationsData = () => {
  return useQuery({
    queryKey: ["inspections-initiations"],
    queryFn: fetchInitiations,
  });
};

export const useIRStatusesData = () => {
  return useQuery({
    queryKey: ["ir-statuses"],
    queryFn: fetchIRStatuses,
  });
};

export const useAttendanceOptionsData = () => {
  return useQuery({
    queryKey: ["attendance-options"],
    queryFn: fetchAttendanceOptions,
  });
};

export const useProjectStatusesData = () => {
  return useQuery({
    queryKey: ["project-statuses"],
    queryFn: fetchProjectStatuses,
  });
};

export const useInspectionsData = () => {
  return useQuery({
    queryKey: ["inspections"],
    queryFn: fetchInspections,
  });
};

export const useInspectionByNumber = (inspectionNumber: string) => {
  return useQuery({
    queryKey: ["inspection", inspectionNumber],
    queryFn: async () => {
      const inspection = await fetchInspection(inspectionNumber);
      const officers = await fetchOfficers(inspection?.id);
      if (inspection.project.abbreviation === UNAPPROVED_PROJECT_ABBREVIATION) {
        inspection.project.id = UNAPPROVED_PROJECT_ID;
        delete inspection.project.abbreviation;
      }
      return { ...inspection, officers };
    },
    enabled: !!inspectionNumber,
  });
};

export const useCreateInspection = (onSuccess: OnSuccessType) => {
  return useMutation({ mutationFn: createInspection, onSuccess });
};
